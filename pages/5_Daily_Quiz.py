import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="EcoSphere | Daily Quiz", page_icon="🌍", layout="centered")

# Custom CSS for a modern "Eco" look
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

/* 🌈 BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #e8f5e9, #e3f2fd, #fce4ec);
    font-family: 'Inter', sans-serif;
}

/* 🔥 FIX TEXT VISIBILITY (ONLY TARGET HEADINGS) */
h1, h2, h3 {
    color: #1b5e20 !important;
    font-weight: 800;
}

/* ❌ REMOVE GLOBAL TEXT OVERRIDE (THIS WAS YOUR BUG) */
/* DO NOT style div, span globally */

/* 🌿 BUTTONS */
.stButton > button {
    border-radius: 25px;
    border: none;
    background: linear-gradient(90deg, #43a047, #66bb6a);
    color: white;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #2e7d32, #43a047);
    transform: scale(1.05);
}

/* 🌟 CARDS */
[data-testid="stVerticalBlock"] > div:has(.element-container) {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

/* 🌍 PROGRESS BAR */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #43a047, #81c784);
}

/* 🎯 RADIO BUTTON FIX (IMPORTANT) */
[data-testid="stRadio"] label {
    color: #263238 !important;   /* 👈 THIS FIXES YOUR ISSUE */
    font-weight: 500;
}

/* 🟢 SELECT BOX TEXT */
[data-testid="stRadio"] div {
    color: #263238 !important;
}

/* 🌈 METRICS */
[data-testid="stMetricValue"] {
    color: #2e7d32 !important;
    font-weight: 800;
}

/* 💡 INFO BOX */
.stInfo {
    background-color: #e3f2fd !important;
    color: #0d47a1 !important;
}

/* 🎉 SUCCESS */
.stSuccess {
    background-color: #e8f5e9 !important;
    color: #1b5e20 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = {}

# ---------------- DATA & LOGIC ----------------
questions = [
    ("🚗 How do you travel daily?", ["Car", "Bike", "Public Transport", "Walk"]),
    ("⚡ Electricity usage?", ["Low", "Medium", "High"]),
    ("🍽️ Food habits?", ["Vegetarian", "Non-Veg", "Vegan"]),
    ("🛒 Shopping frequency?", ["Rare", "Sometimes", "Often"]),
    ("🧴 Plastic usage?", ["Low", "Medium", "High"]),
    ("♻️ Do you recycle?", ["Yes", "No"]),
    ("💧 Water usage?", ["Low", "Medium", "High"]),
    ("📱 Screen time (hours)?", ["<2", "2-5", "5+"])
]

# Corrected & Expanded Carbon Map
carbon_map = {
    "Car": 5.0, "Bike": 2.0, "Public Transport": 1.5, "Walk": 0.1,
    "Low": 1.5, "Medium": 3.0, "High": 5.0,
    "Vegetarian": 2.0, "Non-Veg": 5.0, "Vegan": 1.0,
    "Rare": 1.0, "Sometimes": 2.5, "Often": 4.5,
    "Yes": -2.0, "No": 2.0,
    "<2": 0.5, "2-5": 1.5, "5+": 3.0
}

# ---------------- APP HEADER ----------------
st.title("🌿 EcoSphere")
st.caption("Track your daily footprint and save the planet, one choice at a time.")

# ---------------- QUIZ UI ----------------
if st.session_state.step < len(questions):
    # Progress Bar
    progress = (st.session_state.step) / len(questions)
    st.progress(progress)
    
    q, options = questions[st.session_state.step]
    
    with st.container():
        st.markdown(f"### {q}")
        # Using a selectbox or radio with a clean label
        choice = st.radio("Select your lifestyle choice:", options, index=0, key=f"q_{st.session_state.step}")
        
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("Next ➡️"):
                st.session_state.answers[q] = choice
                st.session_state.step += 1
                st.rerun()

# ---------------- RESULT DASHBOARD ----------------
else:
    st.balloons()
    st.success("✨ Analysis Complete!")
    
    # Logic Calculations
    total_carbon = sum(carbon_map.get(v, 0) for v in st.session_state.answers.values())
    eco_score = max(0, min(100, 100 - (total_carbon * 3))) # Adjusted multiplier for better range

    # High-level Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Carbon Footprint", f"{total_carbon:.1f} kg")
    c2.metric("EcoScore", f"{eco_score:.0f}/100")
    
    if eco_score > 80:
        badge, color = "🌳 Green Master", "#2e7d32"
    elif eco_score > 50:
        badge, color = "🌿 Eco Warrior", "#f9a825"
    else:
        badge, color = "🌱 Eco Seedling", "#d32f2f"
    
    c3.markdown(f"**Rank:** <br> <span style='color:{color}; font-size:20px; font-weight:bold;'>{badge}</span>", unsafe_allow_html=True)

    st.divider()

    # Visualization
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("📊 Footprint Breakdown")
        df = pd.DataFrame({
            'Activity': [q.split(" ")[1] for q in st.session_state.answers.keys()],
            'Impact': [carbon_map.get(v, 0) for v in st.session_state.answers.values()]
        })
        # Matplotlib Plot
        fig, ax = plt.subplots(figsize=(5, 4))
        colors = ['#81c784' if x < 2 else '#ff8a65' for x in df['Impact']]
        ax.barh(df['Activity'], df['Impact'], color=colors)
        ax.set_xlabel('kg CO2')
        st.pyplot(fig)

    with col_right:
        st.subheader("💡 Action Plan")
        tips = []
        if st.session_state.answers.get("🚗 How do you travel daily?") == "Car":
            tips.append("🚗 **Car:** Consider carpooling or an EV.")
        if st.session_state.answers.get("♻️ Do you recycle?") == "No":
            tips.append("♻️ **Recycle:** Start with paper and plastic.")
        if st.session_state.answers.get("🍽️ Food habits?") == "Non-Veg":
            tips.append("🥗 **Diet:** One 'Meatless Monday' saves 10kg CO2.")
        
        if not tips:
            st.write("You're a superstar! Keep doing what you're doing. 🌟")
        else:
            for tip in tips:
                st.info(tip)

    if st.button("🔄 Restart Journey"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()