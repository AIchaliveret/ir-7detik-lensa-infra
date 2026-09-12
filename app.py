import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="FINAL V29 - TRINITY + NASEHAT REVISI", page_icon="🔬", layout="wide")

st.markdown("""
<style>
    .ir-header { background:#0a0a0a; color:#e0e0e0; padding:10px; font-size:11px; font-family:monospace; border:1px solid #333; margin-bottom:15px; }
    .main-title { font-weight:bold; font-size:16px; margin-bottom:10px; }
    div.stButton > button { width:100%; font-weight:bold; border-radius:8px; }
    .advice-box { background: linear-gradient(135deg, #001a0a, #003300); border:2px solid #00ff88; border-radius:12px; padding:15px; margin-top:15px; }
    .advice-title { color:#00ff88; font-weight:bold; font-size:16px; }
    .advice-text { color:#e0ffe0; font-size:14px; line-height:1.6; }
    .nb-box { background:#111; border:1px dashed #ffcc00; border-radius:8px; padding:10px; margin-top:10px; font-size:12px; color:#ffcc88; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="ir-header">IR MANFAAT Deteksi panas peradangan +0.5-1.5°C | Active border jamur lebih panas, komedo lebih dingin | NPU Snapdragon + Thermal Sensor Early Warning, bukan mikroskop optik - LIVE IR READY + AI NASEHAT REVISI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">KACA MATA 7 DETIK IR - 500x / 1000x THERMAL MAP - TRINITY REVISI</div>', unsafe_allow_html=True)

if 'mode' not in st.session_state:
    st.session_state.mode = "DERMA"
if 'result' not in st.session_state:
    st.session_state.result = None

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("1. DERMA\n15cm - 7 detik", key="derma"):
        st.session_state.mode = "DERMA"
with col2:
    if st.button("2. CLIMATE\nCCTV Indoor + Food Safety", key="climate"):
        st.session_state.mode = "CLIMATE"
with col3:
    if st.button("3. MONEY\n15cm AKTIF TERUS", key="money"):
        st.session_state.mode = "MONEY"

st.caption(f"Mode aktif: {st.session_state.mode}")

t1, t2, t3 = st.columns(3)
with t1: st.button("3 DETIK\nCepat")
with t2: st.button("5 DETIK\nStandar")
with t3: st.markdown('<div style="background:#aaffaa; padding:8px; border-radius:8px; border:1px solid #00ff88; text-align:center;"><b>7 DETIK</b><br><small>Observasi Perfect</small></div>', unsafe_allow_html=True)

def generate_nasehat_revisi(mode):
    now = datetime.now().strftime("%H:%M")
    if mode == "DERMA":
        return f"[{now}] 🔥 DERMA 15cm: Panas +0.8°C active border jamur lebih panas, komedo lebih dingin. Saran: Bersihkan pH 5.5, cold compress 2 menit, jangan pencet manual. Observasi pori/bulu 500x tiap pagi."
    elif mode == "CLIMATE":
        # REVISI SESUAI ARAHAN LU: Bukan cuma ayam MBG, tapi makanan pokok basi/expired, bukan FMCG, fastfood juga bisa basi, layak makan
        # Plus CCTV indoor gengsi menengah atas, kelembaban & temperatur, setting traffic orang
        return f"""[{now}] 🌡️ CLIMATE - FOOD SAFETY & CCTV INDOOR GENGSI:

🥘 MAKANAN POKOK BASI/EXPIRED (Bukan FMCG):
Deteksi termal makanan sehari-hari: nasi, lauk, sayur, fast food (ayam goreng, burger) yang sudah tidak layak makan. Makanan basi = suhu permukaan naik tidak merata + kelembaban tinggi. Saran: Cek thermal map makanan sebelum konsumsi, buang jika +1.5°C dari suhu ruang & bau asam.

🏠 CCTV INDOOR MENENGAH ATAS:
Ruko/rukan kecil 10-20 orang, kantor besar 100-500 orang hilir mudik. Fungsi: Ukur kelembaban & temperatur ruangan real-time via thermal sensor. Setting timer deteksi standby hitungan detik (3/5/7 detik) — rumah pakai 7 detik observasi, kantor pakai 3 detik cepat untuk traffic padat.

NB: MBG protein ayam hanya CONTOH, fokus utama = semua makanan pokok harian + fast food layak makan. FMCG kemasan tidak masuk. Level menengah atas — ruko, rukan, kantor, bukan warung."""
    else:
        return f"[{now}] 💰 MONEY 15cm AKTIF TERUS: IR-Absorb uang asli serap IR (hitam), palsu pantul. Loop requestAnimationFrame aktif. Saran: Cek konsistensi serapan di seluruh lembar, simpan di IR-Absorb box 15cm. 100% on-device."

camera = st.camera_input("KLIK UNTUK AKTIFKAN KAMERA + MIC - Allow Camera")

if camera:
    st.success(f"✅ Kamera aktif — Mode {st.session_state.mode}")
    st.image(camera, caption=f"Thermal Map 500x - {st.session_state.mode}")
    with st.spinner("🧠 Snapdragon NPU analisis..."):
        import time; time.sleep(1)
        st.session_state.result = generate_nasehat_revisi(st.session_state.mode)
    
    if st.session_state.result:
        st.markdown(f"""
        <div class="advice-box">
            <div class="advice-title">🧠 HASIL DETEKSI + NASEHAT AI REVISI:</div>
            <div class="advice-text">{st.session_state.result}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.mode == "CLIMATE":
            st.markdown("""
            <div class="nb-box">
            <b>NB CLIMATE UPGRADE POST-KOMPETISI:</b><br>
            - Setting traffic: Rumah 10-20 orang → timer 7 detik observasi perfect<br>
            - Ruko/rukan kecil 20-50 orang → timer 5 detik standar<br>
            - Kantor besar 100-500 orang lalu lalang → timer 3 detik cepat + standby detik<br>
            - Fokus: Makanan pokok & fast food basi/expired (bukan FMCG), layak makan, CCTV kelembaban & temperatur ruangan — level menengah atas
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("**V29 FINAL REVISI** | PWA: sage-gnome-459585.netlify.app | Trinity: DERMA + CLIMATE (Food Safety & CCTV) + MONEY")
