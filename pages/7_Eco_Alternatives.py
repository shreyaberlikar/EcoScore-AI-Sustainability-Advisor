import streamlit as st

st.set_page_config(page_title="Eco Alternatives", layout="wide")

# ---------------- THEME FIX ----------------
st.markdown("""
<style>

/* 🌿 BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #e6f0f3, #f5f9f6);
}

/* 🔥 FIX HEADINGS */
h1, h2, h3 {
    color: #1b5e20 !important;
    font-weight: 800;
}

/* ❌ REMOVE GLOBAL TEXT STYLING */
/* DO NOT use: p, span globally */

/* 💎 CARD STYLE */
.card {
    background: white;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    text-align: center;
}

/* 🎯 FIX TEXT INSIDE CARDS */
.card h3 {
    color: #1b5e20 !important;
    font-size: 18px;
}

.card p {
    color: #37474f !important;
    font-weight: 500;
    font-size: 14px;
}

/* 🌟 EMOJI */
.card .emoji {
    font-size: 30px;
}

/* 🚀 FORCE VISIBILITY */
.card * {
    opacity: 1 !important;
}

/* ✨ OPTIONAL HOVER */
.card:hover {
    transform: translateY(-6px);
    transition: 0.3s;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.title("🌿 Eco Alternatives Guide")
st.caption("Better choices for a greener lifestyle 💚")

# ---------------- PLASTIC ----------------
st.markdown("## 🧴 Plastic Alternatives")

cols = st.columns(4)
plastic_alts = ["🌿 Bamboo", "🥤 Steel", "🍶 Glass", "🛍️ Cloth"]

for i, item in enumerate(plastic_alts):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="emoji">{item}</div>
            <p>Eco-Friendly Option</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- ENERGY ----------------
st.markdown("## ⚡ Energy Efficient Options")

cols = st.columns(3)
energy_alts = ["💡 LED Lights", "🔋 Efficient Appliances", "☀️ Solar Energy"]

for i, item in enumerate(energy_alts):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="emoji">{item}</div>
            <p>Low Energy Usage</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- TRANSPORT ----------------
st.markdown("## 🚚 Transport Alternatives")

cols = st.columns(3)
transport_alts = ["🏡 Local Products", "🚲 Cycling", "🚶 Walking"]

for i, item in enumerate(transport_alts):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="emoji">{item}</div>
            <p>Low Carbon Travel</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- RECYCLING ----------------
st.markdown("## ♻️ Recyclable Materials")

cols = st.columns(3)
recycle_alts = ["📦 Paper", "🧊 Glass", "🪙 Metal"]

for i, item in enumerate(recycle_alts):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="emoji">{item}</div>
            <p>Reusable & Recyclable</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- WASTE ----------------
st.markdown("## 🗑️ Low Waste Options")

cols = st.columns(3)
waste_alts = ["♻️ Refillable", "📉 Minimal Packaging", "🌱 Compostable"]

for i, item in enumerate(waste_alts):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="emoji">{item}</div>
            <p>Reduce Waste</p>
        </div>
        """, unsafe_allow_html=True)
