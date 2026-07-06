import streamlit as st

st.set_page_config(page_title="Eco-Intelligence Hub", layout="wide")

# ---------------- ECO THEME (SAFE CSS) ----------------
st.markdown("""
<style>

/* 🌿 Background (clean but not washed out) */
.stApp {
    background: linear-gradient(135deg, #e8f5e9, #f1f8f4);
}

/* 🔥 FIX TEXT VISIBILITY */
h1, h2, h3, h4 {
    color: #1b5e20 !important;
}

p, span, div {
    color: #263238 !important;
}

/* ✨ CARDS (THIS IS THE MAIN FIX) */
[data-testid="stVerticalBlock"] > div:has(.element-container) {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* 🌱 Metrics styling */
[data-testid="metric-container"] {
    background: #f1f8f4;
    border-radius: 12px;
    padding: 10px;
}

/* 🔥 Buttons */
.stButton > button {
    background: linear-gradient(90deg, #2e7d32, #43a047);
    color: white;
    border-radius: 10px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1b5e20, #2e7d32);
}

/* 🌍 Progress bar color */
.stProgress > div > div > div > div {
    background-color: #2e7d32;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
products = [
    {
        "name": "Artisanal Steel Flask", "type": "Steel", "carbon": 2.1, "score": 88,
        "desc": "Vacuum insulated, 10-year lifespan.", "water": "Saves 40L/yr"
    },
    {
        "name": "Ocean Plastic Tote", "type": "Plastic", "carbon": 5.2, "score": 42,
        "desc": "Made from 100% recycled nylon.", "water": "High Processing"
    },
    {
        "name": "Reclaimed Oak Chair", "type": "Wood", "carbon": 3.5, "score": 75,
        "desc": "Hand-carved from urban timber salvage.", "water": "Net Zero"
    },
    {
        "name": "Boro-Silicate Pitcher", "type": "Glass", "carbon": 1.4, "score": 92,
        "desc": "Infinitely recyclable laboratory grade.", "water": "Saves 120L/yr"
    }
]

# ---------------- HEADER ----------------
st.title("🌿 Eco-Intelligence Dashboard")
st.caption("Track sustainability. Make smarter eco choices.")

# ---------------- TOP INSIGHTS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.success("🌍 CO₂ reduced by 12% this month")
with col2:
    st.info("🏆 Glass = highest EcoScore")
with col3:
    st.warning("⚠️ Plastic impact increasing")

st.divider()

# ---------------- GRID ----------------
cols = st.columns(2)

for i, p in enumerate(products):
    with cols[i % 2]:

        if p["score"] > 70:
            badge = "🟢 Eco-Friendly"
        else:
            badge = "🔴 High Impact"

        with st.container(border=True):

            st.markdown(f"### 🌱 {p['name']}")
            st.caption(f"Material: {p['type']}")

            st.write(p["desc"])

            # Carbon section
            st.write("🌍 **Carbon Impact**")
            st.progress(min(1.0, p["carbon"] / 6))
            st.write(f"{p['carbon']} kg CO₂")

            # Metrics
            c1, c2 = st.columns(2)
            with c1:
                st.metric("EcoScore", p["score"])
            with c2:
                st.metric("Water Impact", p["water"])

            st.write(badge)

            if st.button("View Details →", key=i):
                st.toast(f"Viewing {p['name']} 🌿")

# ---------------- FOOTER ----------------
st.divider()

