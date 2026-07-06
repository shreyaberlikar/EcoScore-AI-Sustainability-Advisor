import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time

# 1. Page Config
st.set_page_config(page_title="EcoScore Predictor", page_icon="🌱", layout="wide")

# 2. Load Model & Assets
warnings.filterwarnings("ignore")
try:
    model = joblib.load("ecoscore_model.pkl")
    features = joblib.load("model_features.pkl")
    scaler = joblib.load("scaler.pkl")
    min_val, max_val = joblib.load("eco_range.pkl")
    training_stats = joblib.load("training_stats.pkl")
except Exception as e:
    st.error(f"Error loading model artifacts: {e}")
    st.stop()

# 3. CSS Styling
st.markdown("""
<style>
    /* Flower Animation */
    .flower-container {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 9999; overflow: hidden;
    }
    .flower {
        position: absolute; top: -50px; font-size: 24px;
        animation: fall 6s linear forwards; opacity: 0;
    }
    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg) translateX(0); opacity: 0; }
        20% { opacity: 1.0; }
        80% { opacity: 1.0; }
        100% { transform: translateY(110vh) rotate(360deg) translateX(50px); opacity: 0; }
    }

    /* Original Layout Styles */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"] {
        overflow: hidden !important;
        height: 100vh;
    }

    [data-testid="stColumn"]:nth-of-type(1) {
        position: fixed;
        width: 32% !important;
        left: 2%; top: 5%; height: 92vh;
        overflow-y: auto !important;
        z-index: 10; padding-right: 15px;
    }

    [data-testid="stColumn"]:nth-of-type(2) {
        margin-left: 36% !important;
        width: 61% !important;
        height: 92vh;
        overflow-y: auto !important;
        padding-right: 20px;
    }

    .compact-card {
        background: white; padding: 20px; border-radius: 20px;
        border-left: 10px solid #2e7d32;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .metric-row { display: flex; justify-content: space-between; align-items: center; margin: 5px 0; }
    .label { font-size: 11px; font-weight: 700; color: #666; text-transform: uppercase; }
    .value { font-size: 28px; font-weight: 900; color: #1b5e20; }
    
    .confidence-low { color: #d32f2f; }
    .confidence-med { color: #f57c00; }
    .confidence-high { color: #388e3c; }

    header {visibility: hidden;}
    .stSlider { margin-bottom: -15px !important; }
</style>
""", unsafe_allow_html=True)

# 4. Initialize History
if "history" not in st.session_state:
    st.session_state["history"] = []

# 5. Layout Columns
col_left, col_right = st.columns([1.2, 2.2])

# 6. Right Side: Sliders
input_data = {}
with col_right:
    st.title("🌱 EcoScore Predictor")
    product_type = st.selectbox("📦 Select Material Type", ["Plastic", "Wood", "Steel", "Glass", "Other"])
    
    tabs = st.tabs(["🌿Raw Material", "🏭Manufacturing", "🚚Transport", "⚡Usage", "♻️End of Life", "🧠System"])
    
    with tabs[0]:
        input_data["raw_material_energy"] = st.slider("Energy", 0.0, 1000.0, 100.0)
        input_data["raw_material_emission_factor"] = st.slider("Emission Factor", 0.0, 2.0, 0.5)
        input_data["raw_material_waste"] = st.slider("Waste", 0.0, 100.0, 10.0)
    with tabs[1]:
        input_data["manufacturing_energy"] = st.slider("Energy", 0.0, 1000.0, 300.0)
        input_data["manufacturing_efficiency"] = st.slider("Efficiency", 0.0, 1.0, 0.7)
        input_data["manufacturing_water_usage"] = st.slider("Water Usage", 0.0, 1000.0, 300.0)
    with tabs[2]:
        input_data["transport_distance_km"] = st.slider("Distance (km)", 0.0, 5000.0, 500.0)
        input_data["transport_mode_factor"] = st.slider("Mode Factor", 0.0, 1.0, 0.2)
        input_data["logistics_energy"] = st.slider("Logistics Energy", 0.0, 500.0, 100.0)
    with tabs[3]:
        input_data["usage_energy_consumption"] = st.slider("Energy Consumption", 0.0, 5000.0, 1000.0)
        input_data["usage_duration_hours"] = st.slider("Usage Duration", 0.0, 10000.0, 2000.0)
        input_data["grid_carbon_intensity"] = st.slider("Grid Carbon Intensity", 0.0, 1000.0, 300.0)
    with tabs[4]:
        input_data["recycling_efficiency"] = st.slider("Recyclability", 0.0, 1.0, 0.5)
        input_data["disposal_emission_factor"] = st.slider("Disposal Emission", 0.0, 5.0, 1.0)
        input_data["recovered_material_value"] = st.slider("Recovered Value", 0.0, 100.0, 20.0)
    with tabs[5]:
        input_data["state_complexity_index"] = st.slider("Complexity Index", 0.0, 1.0, 0.5)
        input_data["policy_action_score"] = st.slider("Policy Score", -1.0, 1.0, 0.0)
        input_data["optimization_reward_signal"] = st.slider("Optimization Signal", 0.0, 20.0, 5.0)

# Feature Engineering aligned with setup
df_raw = pd.DataFrame([input_data])

# Engineered Features
weight_map = {'Plastic': 1.5, 'Steel': 1.2, 'Other': 1.0, 'Glass': 0.8, 'Wood': 0.5}
df_raw['product_type'] = product_type
df_raw['material_weight_factor'] = df_raw['product_type'].map(weight_map)
usage_dur = df_raw['usage_duration_hours'].replace(0, 1)
df_raw['carbon_intensity'] = df_raw['usage_energy_consumption'] / usage_dur
df_raw['transport_impact'] = df_raw['transport_distance_km'] * df_raw['transport_mode_factor']
df_raw['recyclability_score'] = df_raw['recycling_efficiency']

# Setup exact columns matching the trained model 
df_encoded = pd.get_dummies(df_raw, columns=['product_type'], prefix='type', dtype=int)
df_input = df_encoded.reindex(columns=features, fill_value=0)

try:
    # Scale Data
    X_scaled = scaler.transform(df_input)
    # Predict
    carbon = model.predict(X_scaled)[0]
    
    # Confidence Score (Euclidean distance to training mean)
    # Distance to training mean divided by number of features roughly
    dist = np.linalg.norm(X_scaled[0] - training_stats['mean'])
    max_expected_dist = np.linalg.norm(training_stats['std'] * 3) # 3 std approx limit
    conf_score = max(0, min(100, 100 * (1 - (dist / max_expected_dist))))
    
    # Calculate EcoScore
    if max_val != min_val:
        eco_score = max(0, min(100, 100 * (1 - (carbon - min_val) / (max_val - min_val))))
    else:
        eco_score = 50.0

except Exception as e:
    st.error(f"Prediction Error: {e}")
    st.stop()

# 8. Left Side: Display Results & History
with col_left:
    st.markdown(f"""
    <div class="compact-card">
        <h4 style="margin:0; color:#1b5e20;">Live Assessment</h4>
    </div>""", unsafe_allow_html=True)
    
    # GAUGE METER FOR ECOSCORE
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = eco_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "EcoScore", 'font': {'size': 20, 'color':'#2e7d32'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "rgba(0,0,0,0.1)"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': "#ef5350"},    # Red
                {'range': [40, 70], 'color': "#ffca28"},   # Yellow
                {'range': [70, 100], 'color': "#66bb6a"}   # Green
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': eco_score
            }
        }
    ))
    fig_gauge.update_layout(height=220, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # BAR CHART FOR COMPONENTS
    components = ['Materials', 'Manufacturing', 'Transport', 'Usage']
    values = [
        input_data['raw_material_energy'] * input_data['raw_material_emission_factor'] * weight_map[product_type],
        input_data['manufacturing_energy'] / max(0.1, input_data['manufacturing_efficiency']),
        input_data['transport_distance_km'] * input_data['transport_mode_factor'],
        input_data['usage_energy_consumption']
    ]
    # Normalize for display
    tot = sum(values) + 1
    values = [v/tot * carbon for v in values] # Estimated component contribution to carbon
    
    fig_bar, ax = plt.subplots(figsize=(5, 3))
    ax.bar(components, values, color=['#43a047', '#ffb300', '#1e88e5', '#e53935'])
    ax.set_ylabel('Est. Carbon (kg CO2)')
    ax.set_title('Impact Breakdown')
    plt.xticks(rotation=25, ha='right', fontsize=9)
    plt.tight_layout()
    st.pyplot(fig_bar)

    st.markdown(f"""
    <div class="compact-card" style="margin-top: -10px;">
        <div class="metric-row">
            <span class="label">🌍 Footprint</span>
            <span class="value" style="color: #d32f2f;">{carbon:.1f} kg</span>
        </div>
        <div class="metric-row">
            <span class="label">🎯 AI Confidence</span>
            <span class="value" style="font-size:18px;">{conf_score:.1f}%</span>
        </div>
    </div>""", unsafe_allow_html=True)

    # Save History Button
    if st.button("🚀 Save Prediction", use_container_width=True):
        st.session_state["history"].append({
            "Product": product_type,
            "EcoScore": round(eco_score, 1),
            "Carbon": round(carbon, 1),
            "Confidence": f"{round(conf_score, 1)}%"
        })
        st.session_state["last_input"] = input_data 
        st.session_state["eco_score"] = round(eco_score, 2)
        
        # TRIGGER FADED FLOWERS
        flower_html = """
        <div class="flower-container">
            <div class="flower" style="left:10%; animation-delay:0s;">🌸</div>
            <div class="flower" style="left:25%; animation-delay:1.5s;">🌼</div>
            <div class="flower" style="left:45%; animation-delay:0.5s;">🌸</div>
            <div class="flower" style="left:65%; animation-delay:2s;">🌼</div>
            <div class="flower" style="left:85%; animation-delay:1s;">🌸</div>
        </div>
        """
        st.markdown(flower_html, unsafe_allow_html=True)
        st.success("Analysis Saved!")

    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

    if st.session_state["history"]:
        st.write("---")
        st.markdown("### 📜 History")
        st.dataframe(pd.DataFrame(st.session_state["history"]).tail(5), use_container_width=True, height=150)
        
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state["history"] = []
            st.rerun()