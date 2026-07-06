import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Why EcoScore?", layout="wide")

# ---------------- 💎 STRONG UI FIX (NO FADE EVER) ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #dff6e3, #e3f2fd, #fff8e1);
    font-family: 'Inter', sans-serif;
}

/* 🔥 TEXT FIX */
h1, h2, h3, h4 {
    color: #1b5e20 !important;
    font-weight: 800;
}

p, span, label {
    color: green !important;
    font-size: 15px;
}

/* 💎 CARD STYLE */
.card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

/* 🌈 HERO BOX */
.hero {
    background: linear-gradient(90deg, #43a047, #66bb6a);
    color: white;
    padding: 18px;
    border-radius: 18px;
    font-size: 18px;
    font-weight: 600;
}

/* 📊 CHART BOX */
.chart-box {
    background: white;
    padding: 15px;
    border-radius: 15px;
}

/* 💡 TIP BOX */
.tip {
    background: #e8f5e9;
    padding: 12px;
    border-radius: 12px;
    margin-top: 10px;
}
/* 💎 FORCE ALL TEXT INSIDE CARD */
.card * {
    color: #1b5e20 !important;   /* dark green */
    opacity: 1 !important;
}

/* ✨ DESCRIPTION TEXT */
.card p {
    color: #37474f !important;   /* dark grey */
    font-size: 15px;
}

/* 🌟 HEADING */
.card h3 {
    color: #1b5e20 !important;
    font-weight: 700;
}

/* 💡 TIP BOX */
.card .tip {
    background: #e8f5e9;
    color: #1b5e20 !important;
    font-weight: 600;
    padding: 10px;
    border-radius: 10px;
}

/* 🧊 REMOVE FADE */
.card {
    opacity: 1 !important;
}
.card:nth-child(1) { border-left: 5px solid #ff7043; }
.card:nth-child(2) { border-left: 5px solid #ffca28; }
.card:nth-child(3) { border-left: 5px solid #66bb6a; }
.card:nth-child(4) { border-left: 5px solid #42a5f5; }
.card:nth-child(5) { border-left: 5px solid #ab47bc; }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🔍 Why this EcoScore?")
st.caption("Let’s break down what really affects your sustainability 🌱")

# ---------------- HERO INSIGHT ----------------
st.markdown("""
<div class="hero">
💡 Most products lose EcoScore due to <b>transport 🚚 and manufacturing ⚡</b> — these two alone can contribute over 50% of emissions.
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- PIE + BAR ----------------
col1, col2 = st.columns(2)

factors = {
    "🚚 Transport": 30,
    "⚡ Manufacturing": 25,
    "♻️ Waste": 20,
    "🔌 Usage": 15,
    "🌿 Recycling": 10
}

labels = list(factors.keys())
values = list(factors.values())

with col1:
    st.markdown("### 📊 Impact Distribution")
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.0f%%")
    st.pyplot(fig)

with col2:
    st.markdown("### 📈 Impact Comparison")
    fig2, ax2 = plt.subplots()
    ax2.barh(labels, values)
    ax2.set_xlabel("Impact %")
    st.pyplot(fig2)

# ---------------- STORY EXPLANATION ----------------
st.markdown("## 🧠 Real Example (Understand Like a Pro)")

st.markdown("""
<div class="card">
<b>Example:</b> You bought a plastic bottle from another country 🌍

👉 Transport 🚚 = Long distance → HIGH emissions  
👉 Manufacturing ⚡ = Plastic processing → HIGH energy  
👉 Recycling 🌿 = Low → BAD impact  

💥 Result: EcoScore drops significantly
</div>
""", unsafe_allow_html=True)

# ---------------- FACTOR CARDS ----------------
st.markdown("## 🔍 Deep Dive Into Each Factor")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>🚚 Transport</h3>
    Longer shipping distance = more fuel burned = more CO₂  
    <div class="tip">💡 Choose local products</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>⚡ Manufacturing</h3>
    High energy factories increase footprint  
    <div class="tip">💡 Prefer energy-efficient brands</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>♻️ Waste</h3>
    More waste = more pollution  
    <div class="tip">💡 Reduce material usage</div>
    </div>
    """, unsafe_allow_html=True)

c4, c5 = st.columns(2)

with c4:
    st.markdown("""
    <div class="card">
    <h3>🔌 Usage</h3>
    Energy during use adds emissions  
    <div class="tip">💡 Use efficient devices</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card">
    <h3>🌿 Recycling</h3>
    Better recycling = higher EcoScore  
    <div class="tip">💡 Recycle properly</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- GOOD VS BAD ----------------
st.markdown("## ⚖️ Good vs Bad")

colA, colB = st.columns(2)

with colA:
    st.success("✅ Good Choices")
    st.write("• Local products 🚚")
    st.write("• Low energy production ⚡")
    st.write("• High recycling ♻️")

with colB:
    st.error("❌ Bad Choices")
    st.write("• Imported goods 🚚")
    st.write("• High waste ♻️")
    st.write("• No recycling 🌿")

# ---------------- FINAL ----------------
st.markdown("## 🌱 Final Tip")

st.info("Even small choices like choosing local or reducing plastic can boost your EcoScore massively 💚")
