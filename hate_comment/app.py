import streamlit as st
from pathlib import Path
import base64
import os

st.set_page_config(
    page_title="Hate Comment Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_file = Path(__file__).parent / "style.css"
if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text()}</style>",
        unsafe_allow_html=True
    )
else:
    st.warning("style.css tidak ditemukan")


BASE_DIR = Path(__file__).resolve().parent
hero_image_path = BASE_DIR / "assets" / "hero.jpg"

if hero_image_path.exists():
    encoded_image = base64.b64encode(hero_image_path.read_bytes()).decode()

    st.markdown(
        f"""
        <div class="hero-container">
            <img src="data:image/jpg;base64,{encoded_image}" class="hero-img"/>
            <div class="hero-overlay"></div>
            <div class="hero-text">
                <h1>Hate Comment<br>Detection</h1>
                <p>
                    Sistem pendeteksi komentar berbasis Natural Language Processing
                    untuk mengklasifikasikan komentar Netral dan Hate secara otomatis.
                </p>
                <a href="Deteksi" class="hero-btn">Mulai Deteksi</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("File hero.jpg tidak ditemukan di folder assets/")

    

st.markdown("## Rising Problem We Face")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(
        """
        <p class="problem-text">
        Pesatnya pertumbuhan penggunaan media sosial, khususnya Twitter, di Indonesia menyebabkan meningkatnya penyebaran komentar bermuatan ujaran kebencian. Karakteristik Twitter yang real-time, terbuka, dan anonim membuat moderasi konten secara manual menjadi tidak efektif karena volume data yang besar dan variasi bahasa yang tidak baku. Oleh karena itu, diperlukan sistem deteksi otomatis berbasis Natural Language Processing (NLP), sehingga penelitian ini membandingkan kinerja algoritma Multinomial Naive Bayes dan Neural Network Multi-Layer Perceptron (MLP) dalam mendeteksi hate comment bahasa Indonesia.
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "assets", "problem2.png")

    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.warning("Gambar problem2.png tidak ditemukan")

st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Our Solutions</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

def get_base64_img(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img1 = f"data:image/png;base64,{get_base64_img(os.path.join(BASE_DIR,'assets','solution_1.png'))}"
img2 = f"data:image/png;base64,{get_base64_img(os.path.join(BASE_DIR,'assets','solution_2.png'))}"
img3 = f"data:image/png;base64,{get_base64_img(os.path.join(BASE_DIR,'assets','solution_3.png'))}"

with c1:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img1}" class="card-img"/>
            <div class="card-content">
                <h3>Report & Analysis</h3>
                <p>Menyediakan hasil analisis klasifikasi komentar ke dalam kategori Netral dan Hate berdasarkan pemrosesan teks otomatis.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img2}" class="card-img"/>
            <div class="card-content">
                <h3>Educate & Prevent</h3>
                <p>Mendukung pencegahan ujaran kebencian melalui teknologi NLP.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img3}" class="card-img"/>
            <div class="card-content">
                <h3>Easy to Use</h3>
                <p>Antarmuka sederhana dan intuitif untuk melakukan analisis komentar dengan cepat dan mudah.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)



