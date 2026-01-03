import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Hate Comment Detection",
        initial_sidebar_state="collapsed",
    layout="wide"
    )

def load_css():
    if Path("style.css").exists():
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

@st.cache_resource
def load_assets():
    try:
        tfidf = joblib.load("models/tfidf.pkl")
        model = joblib.load("models/mlp_model.pkl")
        le = joblib.load("models/label_encoder.pkl")
        return tfidf, model, le
    except:
        return None, None, None

tfidf, model, le = load_assets()

if st.button("⬅\nKembali"):
    st.switch_page("app.py")

st.markdown('<h1 style="color:#ffb800; font-size:3.5rem; font-weight:800; margin-top:10px;">Hate Comment Detection</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#white; opacity: 80%; margin-bottom:20px;">Sistem ini menganalisis teks komentar menggunakan pendekatan Natural Language Processing untuk menentukan apakah komentar termasuk Netral atau Hate.</p>', unsafe_allow_html=True)

st.markdown('<div class="scanner-container">', unsafe_allow_html=True)

st.markdown('<p style="color:white; font-weight:600; margin-bottom:10px;">Masukkan Komentar disini:</p>', unsafe_allow_html=True)

user_input = st.text_area("input", label_visibility="collapsed", height=150)

if st.button("🔍 Analysis Sekarang"):
    if user_input.strip():
    
        vec = tfidf.transform([user_input])
        label = le.inverse_transform(model.predict(vec))[0]
        confidence = model.predict_proba(vec).max() * 100

        color = "#ef4444" if label.lower() == "hate" else "#22c55e"
        bg = "result-hate" if label.lower() == "hate" else "result-neutral"
        status = "⚠️ TERDETEKSI: HATE" if label.lower() == "hate" else "✅ AMAN: NEUTRAL"
        
        st.markdown(f"""
            <div class="result-card {bg}">
                <div>
                    <h2 style="color:{color}; margin:0; font-weight:800;">{status}</h2>
                    <p style="color:white; opacity:0.8;">Komentar dianalisis sebagai {label.lower()}.</p>
                </div>
                <div style="text-align:right;">
                    <div class="percentage-text" style="color:{color};">{confidence:.1f}%</div>
                    <div style="color:{color}; font-weight:bold; font-size:0.8rem;">Confidence Score</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Silakan masukkan teks.")

st.markdown('</div>', unsafe_allow_html=True)