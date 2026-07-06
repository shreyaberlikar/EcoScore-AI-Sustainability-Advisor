import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Eco Insights", layout="wide", page_icon="🌱")

# ------------------ ADVANCED STYLING + FALLING AUTUMN LEAVES ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

/* 🌿 BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #fdfaf6, #f1f8f4);
    font-family: 'Inter', sans-serif;
}

/* 🔥 TEXT VISIBILITY FIX */
h1, h2, h3 {
    color: #1b5e20 !important;
    font-weight: 800;
}

p, span, label {
    color: #263238 !important;
}

/* 🌱 METRICS */
[data-testid="stMetricValue"] {
    color: #2e7d32 !important;
    font-weight: 800;
}

/* ✨ CARD EFFECT */
[data-testid="stVerticalBlock"] > div:has(.element-container) {
    background: white;
    border-radius: 16px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

/* 📊 CHART AREA */
.stAltairChart {
    background: white;
    border-radius: 12px;
    padding: 10px;
}

/* ⚠️ ALERT FIX */
.stAlert {
    color: #000 !important;
}

/* 🌿 SIDEBAR */
[data-testid="stSidebar"] {
    background: #f5f9f6 !important;
}

/* 🌍 PROGRESS BAR */
.stProgress > div > div > div > div {
    background-color: #2e7d32;
}

/* 🍃 LEAF ANIMATION */
.leaf-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.leaf {
    position: absolute;
    top: -50px;
    font-size: 22px;
    animation: fall 10s linear infinite;
    opacity: 0.7;
}

/* 🍂 FALLING EFFECT */
@keyframes fall {
    0% {
        transform: translateY(0) rotate(0deg) translateX(0);
        opacity: 0;
    }
    10% { opacity: 0.7; }
    90% { opacity: 0.7; }
    100% {
        transform: translateY(110vh) rotate(360deg) translateX(80px);
        opacity: 0;
    }
}
</style>

<!-- 🌿 LEAF HTML -->
<div class="leaf-container">
    <div class="leaf" style="left: 5%; animation-delay: 0s;">🍃</div>
    <div class="leaf" style="left: 20%; animation-delay: 2s;">🌿</div>
    <div class="leaf" style="left: 40%; animation-delay: 4s;">🍃</div>
    <div class="leaf" style="left: 60%; animation-delay: 1s;">🌿</div>
    <div class="leaf" style="left: 80%; animation-delay: 3s;">🍃</div>
    <div class="leaf" style="left: 95%; animation-delay: 5s;">🌿</div>
</div>

""", unsafe_allow_html=True)

# --- UI Header ---
st.title("🌱 EcoScore Insights Dashboard")
st.markdown("### Lifecycle Analysis & Sustainability Optimization")
st.divider()

# ---------------- DATA VALIDATION ----------------
if "last_input" not in st.session_state:
    st.warning("⚠️ No data found. Please run a prediction first to view insights.")
    st.stop()

data = st.session_state["last_input"]
current_score = st.session_state.get("eco_score", 50)

# ---------------- REAL-TIME SIMULATOR (SIDEBAR) ----------------
st.sidebar.header("🛠️ Optimization Sandbox")
st.sidebar.write("Simulate changes to see potential score impact.")
opt_transport = st.sidebar.slider("Optimize Transport (%)", 0, 100, 0)

reduction_factor = 1 - (opt_transport / 100)
simulated_score = min(current_score + (opt_transport // 10), 100)

# ---------------- TOP METRICS ----------------
m1, m2, m3, m4 = st.columns(4)
m1.metric("Projected EcoScore", f"{simulated_score}/100", delta=f"{simulated_score - current_score if opt_transport > 0 else ''}")
m2.metric("Energy usage", f"{data['manufacturing_energy']} kWh", delta="-5%", delta_color="inverse")
m3.metric("Waste Rate", f"{data['raw_material_waste']}%", delta="High", delta_color="off")
m4.metric("Recycling", f"{int(data['recycling_efficiency']*100)}%", delta="Target: 80%")

st.write("") 

# ---------------- VISUAL ANALYSIS (ALTAIR) ----------------
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📊 Environmental Impact Breakdown")
    
    impact_dict = {
        "Stage": ["Raw Material", "Manufacturing", "Transport", "Usage"],
        "Impact Score": [
            data["raw_material_energy"],
            data["manufacturing_energy"],
            (data["transport_distance_km"] * data["transport_mode_factor"]) * reduction_factor,
            data["usage_energy_consumption"]
        ]
    }
    df_impact = pd.DataFrame(impact_dict)

    chart = alt.Chart(df_impact).mark_bar(cornerRadiusEnd=4, size=30).encode(
        x=alt.X('Impact Score:Q', title="Calculated Impact Units"),
        y=alt.Y('Stage:N', sort='-x', title=None),
        color=alt.condition(
            alt.datum['Impact Score'] == df_impact['Impact Score'].max(),
            alt.value('#e74c3c'), 
            alt.value('#d2691e') 
        )
    ).properties(height=300)

    st.altair_chart(chart, use_container_width=True)

with col_right:
    st.subheader("🎯 Key Finding")
    max_stage = df_impact.loc[df_impact['Impact Score'].idxmax(), 'Stage']
    
    with st.container(border=True):
        st.error(f"**Primary Bottleneck: {max_stage}**")
        st.write(f"Your highest carbon footprint originates from the **{max_stage}** phase.")
        if opt_transport > 0:
            st.info(f"Applying **{opt_transport}%** optimization to Transport...")
        st.caption("Reducing the bottleneck phase boosts your overall EcoScore significantly.")

# ---------------- IMPROVEMENT ROADMAP ----------------
st.divider()
st.subheader("🧠 Actionable Sustainability Roadmap")

step1, step2, step3 = st.columns(3)

with step1:
    with st.expander("📍 Phase 1: Immediate", expanded=True):
        if data["transport_distance_km"] > 1000:
            st.info("🚚 **Logistics**\n\nSwitch to local suppliers to reduce transit CO2.")
        else:
            st.success("🚚 **Logistics**\n\nTransport distance is within optimal limits.")

with step2:
    with st.expander("⚙️ Phase 2: Structural", expanded=True):
        if data["manufacturing_energy"] > 500:
            st.warning("⚡ **Energy**\n\nTransition to renewable-powered facilities.")
        else:
            st.success("⚡ **Energy**\n\nManufacturing efficiency is performing well.")

with step3:
    with st.expander("♻️ Phase 3: Circular", expanded=True):
        if data["recycling_efficiency"] < 0.6:
            st.error("🔄 **Waste**\n\nRedesign for easier disassembly/recycling.")
        else:
            st.success("🔄 **Waste**\n\nCircular metrics meet industry standards.")

# ---------------- NAVIGATION FOOTER ----------------
st.write("") # Spacer
c1, c2, c3 = st.columns([1, 1, 1])
with c2: # Center the button
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.divider()
if st.sidebar.button("🏠 Back to Home", use_container_width=True, key="sidebar_home"):
    st.switch_page("app.py")