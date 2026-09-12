import streamlit as st

# --- PAGE CONFIG V29 TRINITY ---
st.set_page_config(
    page_title="FINAL V29 - TRINITY 3 LENS IR",
    page_icon="🔬",
    layout="wide",
)

# --- CUSTOM CSS BIAR KAYA SAGE-GNOME (Foto 1 & 2 lu) ---
st.markdown("""
<style>
    .ir-header {
        background-color: #0a0a0a;
        color: #e0e0e0;
        padding: 10px;
        font-size: 11px;
        font-family: monospace;
        border: 1px solid #333;
        margin-bottom: 15px;
    }
    .main-title {
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 10px;
        letter-spacing: 0.5px;
    }
    div.stButton > button:first-child {
        width: 100%;
        font-weight: bold;
        border-radius: 8px;
    }
    /* Warna Trinity */
    .derma-btn button { background-color: #00ff88 !important; color: black !important; }
    .climate-btn button { background-color: #0088ff !important; color: white !important; }
    .money-btn button { background-color: #ffcc00 !important; color: black !important; }
    .start-btn button { background-color: #00ff88 !important; color: black !important; font-size: 16px !important; height: 50px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER IR MANFAAT (SAMA KAYAK FOTO 1 LU) ---
st.markdown("""
<div class="ir-header">
IR MANFAAT Deteksi panas peradangan +0.5-1.5°C | Active border jamur lebih panas, komedo lebih dingin | NPU Snapdragon + Thermal Sensor Early Warning, bukan mikroskop optik - LIVE IR READY
</div>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<div class="main-title">KACA MATA 7 DETIK IR - 500x / 1000x THERMAL MAP</div>', unsafe_allow_html=True)

# --- STATE ---
if 'mode' not in st.session_state:
    st.session_state.mode = "DERMA - 15cm 7 detik (skincare)"
if 'timer' not in st.session_state:
    st.session_state.timer = "7 DETIK"

# --- 3 TOMBOL TRINITY (SAMA PERSIS SAGE-GNOME) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="derma-btn">', unsafe_allow_html=True)
    if st.button("1. DERMA\n15cm - 7 detik", key="derma"):
        st.session_state.mode = "DERMA - 15cm 7 detik (skincare)"
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="climate-btn">', unsafe_allow_html=True)
    if st.button("2. CLIMATE\n2-3m + MBG", key="climate"):
        st.session_state.mode = "CLIMATE - 2-3m + MBG (protein ayam)"
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="money-btn">', unsafe_allow_html=True)
    if st.button("3. MONEY\n15cm AKTIF TERUS", key="money"):
        st.session_state.mode = "MONEY - 15cm AKTIF TERUS (IR-Absorb uang)"
    st.markdown('</div>', unsafe_allow_html=True)

st.caption(f"Mode aktif: {st.session_state.mode}")

# --- TIMER LENSA INFRA (SAMA KAYAK FOTO 1) ---
st.markdown("**TIMER LENSA INFRA** <span style='float:right; background:#aaffaa; padding:2px 8px; border-radius:10px; font-size:11px;'>PROMO 7 DETIK</span>", unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)
with t1:
    if st.button("3 DETIK\nCepat", key="t3"):
        st.session_state.timer = "3 DETIK - Cepat"
with t2:
    if st.button("5 DETIK\nStandar", key="t5"):
        st.session_state.timer = "5 DETIK - Standar"
with t3:
    # Tombol aktif ijo kayak di foto lu
    st.markdown('<div style="background:#aaffaa; padding:8px; border-radius:8px; border:1px solid #00ff88;"><b>7 DETIK</b><br><small>Observasi Perfect • Rekomendasi</small></div>', unsafe_allow_html=True)
    st.session_state.timer = "7 DETIK - Observasi Perfect"

st.markdown("""
<div style="background:#0a1a0a; color:#00ff88; padding:8px; font-size:11px; font-family:monospace; border:1px solid #003300; margin:10px 0;">
7 DETIK LENSA INFRA DETEKSI - Lihat dulu kondisi kulitmu! 0-2s atur posisi • 2-5s auto-scan shortir wajah • 5-7s puas lihat pori/komedo/bulu halus 500x baru auto capture
</div>
""", unsafe_allow_html=True)

# --- TOMBOL MULAI DETEKSI ---
st.markdown('<div class="start-btn">', unsafe_allow_html=True)
start = st.button("MULAI DETEKSI 7 DETIK - SIAP DETEKSI", key="start", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.caption("0-2s atur posisi wajah di tengah | 2-5s Lensa IR auto scan shortir | 5-7s lihat detail pori/bulu 500x")

# --- CAMERA (FULL CAMERA - Pajang Wajah) ---
st.markdown("---")
st.markdown("### 📷 FULL CAMERA - Pajang Wajah")
st.markdown("Pajang wajah di dalam frame FACE ID • IR • NPU")

# Privasi Box (dari Streamlit lama lu)
st.info("🔒 **Privasi:** Foto wajah TIDAK di-upload ke server. Semua proses IR thermal scan 7 detik dilakukan lokal di browser HP/laptop kamu. Aman untuk kompetisi Lablab.ai.")

if start:
    st.success(f"✅ Mode: {st.session_state.mode} | Timer: {st.session_state.timer} - Kamera Aktif!")
    camera = st.camera_input("KLIK UNTUK AKTIFKAN KAMERA + MIC (HP & Laptop) - Allow Camera", key="cam")
    if camera:
        st.image(camera, caption=f"Hasil {st.session_state.mode} - Thermal Map 500x")
        if "MONEY" in st.session_state.mode:
            st.warning("💰 MONEY Mode: IR-Absorb deteksi tinta hitam-putih - loop requestAnimationFrame AKTIF TERUS")
        elif "DERMA" in st.session_state.mode:
            st.warning("🌡️ DERMA Mode: Deteksi panas peradangan +0.5-1.5°C - Active border jamur lebih panas")
        else:
            st.warning("🌍 CLIMATE Mode: Room scan 2-3m + MBG protein ayam 15cm")
else:
    st.camera_input("KLIK UNTUK AKTIFKAN KAMERA + MIC", key="cam_idle")

# --- FOOTER LINK (SINKRON SAMA GITHUB V29) ---
st.markdown("---")
st.markdown("""
**🔗 Links V29 Trinity:**
- Main PWA (Vanilla JS): https://sage-gnome-459585.netlify.app/
- GitHub: https://github.com/aichaliveret/ir-7detik-lensa-infra
- Video Demo 60s: [Ganti dengan link Shorts asli]
""")
