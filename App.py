import streamlit as st

# Page Config
st.set_page_config(page_title="EcoScore AI", layout="wide", page_icon="🌱")

# ------------------ ADVANCED STYLING (Refined for Beauty) ------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* Falling Leaf Animation */
    .leaf-container {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 0; overflow: hidden;
    }
    .leaf {
        position: absolute; top: -50px; font-size: 24px;
        animation: fall 10s linear infinite; opacity: 0.6;
    }
    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.6; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }

    /* Smooth page entry animation */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stApp {
        background: radial-gradient(circle at top right, #fdfbfb 0%, #ebedee 100%), 
                    linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%);
        font-family: 'Inter', sans-serif;
    }

    .animate-fade {
        animation: fadeInUp 0.8s ease-out forwards;
    }

    .main-title {
        background: linear-gradient(90deg, #1b5e20, #43a047);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 72px;
        font-weight: 800;
        text-align: left;
        margin-bottom: 0px;
        letter-spacing: -2px;
    }

    .subtitle {
        font-size: 22px;
        color: #4e5d52;
        text-align: left;
        margin-bottom: 30px;
        font-weight: 400;
        line-height: 1.4;
    }

    /* Modern Glassmorphism Card */
    .card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 35px;
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .card:hover {
        transform: translateY(-10px) scale(1.02);
        background: #D5E5D5;
        border: 1px solid rgba(46, 125, 50, 0.4);
        box-shadow: 0 20px 40px rgba(46, 125, 50, 0.1);
    }

    .feature-title {
        font-size: 24px;
        font-weight: 800;
        color: #1b5e20;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    /* BEAUTIFUL PULSING BUTTON */
    div.stButton > button {
        background: linear-gradient(90deg, #2e7d32, #43a047);
        color: white;
        border-radius: 14px;
        padding: 14px 35px;
        font-weight: 700;
        border: none;
        box-shadow: 0 0 0 0 rgba(46, 125, 50, 0.7);
        animation: pulse 2s infinite;
        transition: all 0.3s ease;
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(46, 125, 50, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(46, 125, 50, 0); }
        100% { box-shadow: 0 0 0 0 rgba(46, 125, 50, 0); }
    }

    div.stButton > button:hover {
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.3);
        transform: translateY(-2px);
        background: linear-gradient(90deg, #1b5e20, #2e7d32);
    }

    .footer {
        text-align: center;
        color: #667c6b;
        padding: 60px 0;
        font-size: 15px;
        font-weight: 500;
    }
    
    .block-container {
        padding-top: 3rem;
    }
</style>

<div class="leaf-container">
    <div class="leaf" style="left: 10%; animation-delay: 0s;">🍃</div>
    <div class="leaf" style="left: 35%; animation-delay: 2s;">🌿</div>
    <div class="leaf" style="left: 70%; animation-delay: 4s;">🍃</div>
    <div class="leaf" style="left: 90%; animation-delay: 1s;">🌿</div>
</div>
""", unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------

st.markdown('<div class="animate-fade">', unsafe_allow_html=True)
hero_col1, hero_col2 = st.columns([2, 1])

with hero_col1:
    st.markdown('<div class="main-title">🌱 EcoScore AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Shop smarter, live greener. Get instant environmental impact ratings for your favorite products.</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        if st.button("🚀 Analyze a Product"):
            st.switch_page("pages/1_Predict.py") 
            
    with c2:
        st.caption("Join 5,000+ eco-conscious shoppers making a difference today.")

with hero_col2:
    st.markdown("""
    <style>
        .hero-img { animation: float 6s ease-in-out infinite; }
        @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-20px); } 100% { transform: translateY(0px); } }
    </style>
    """, unsafe_allow_html=True)
    st.image("Vector Energy Saving Caring For The Earth PNG Images,  Vector, Power Windmill, Renewable Energy PNG Transparent Background - Pngtree.jpeg", use_container_width=True)

st.write("---")
st.markdown('</div>', unsafe_allow_html=True)

# ------------------ RELEVANT INFO CARDS ------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card animate-fade" style="animation-delay: 0.1s;">
        <div class="feature-title">🌍 Carbon Footprint</div>
        <p style="color: #4e5d52; font-size: 16px;">See the total planet-warming gases emitted to make, ship, and sell your product.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card animate-fade" style="animation-delay: 0.2s;">
        <div class="feature-title">📊 EcoScore</div>
        <p style="color: #4e5d52; font-size: 16px;">A simple 0–100 rating that grades how "green" a product really is, from A+ to F.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card animate-fade" style="animation-delay: 0.3s;">
        <div class="feature-title">💡 Better Choices</div>
        <p style="color: #4e5d52; font-size: 16px;">Discover similar products with lower environmental impact and better sustainability scores.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ------------------ WHY & HOW SECTION ------------------
col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="card animate-fade" style="animation-delay: 0.4s;">
        <h3 style='color: #1b5e20; font-weight: 800;'>🌿 Why use EcoScore?</h3>
        <p>We help you cut through the marketing noise and "green" labels:</p>
        <ul style='color: #4e5d52; line-height: 1.8;'>
            <li><b>Verified Data:</b> We look past the packaging to find the truth.</li>
            <li><b>Track Progress:</b> Watch your personal carbon footprint drop over time.</li>
            <li><b>Support Ethics:</b> Reward brands that actually care about the Earth.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card animate-fade" style="animation-delay: 0.5s;">
        <h3 style='color: #1b5e20; font-weight: 800;'>⚙️ How to Start</h3>
        <ol style='color: #4e5d52; line-height: 1.8;'>
            <li><b>Search:</b> Type in a product name or scan a barcode.</li>
            <li><b>Review:</b> Check the score for carbon, water usage, and ethics.</li>
            <li><b>Decide:</b> Buy with confidence or find a better eco-friendly alternative.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown('<div class="footer">EcoScore AI © 2026 | Dedicated to a Sustainable Future 🌱</div>', unsafe_allow_html=True)