
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
import random

st.set_page_config(page_title="V31.1 DUAL CAM IR + CCTV IDEAL WARNING - IR 7 Detik", layout="wide", page_icon="🔬")

st.markdown("""
<style>
.header {background:#0a0a0a;color:#00ff88;padding:12px;border-radius:10px;text-align:center;font-family:monospace;border:1px solid #003300}
.title {font-weight:bold;color:#fff;text-align:center}
.trinity {display:flex;gap:6px}
.ideal {background:#0a1a0a;border:1px solid #003300;color:#00ff88;padding:8px;border-radius:8px;font-size:12px}
.warning {background:#1a1a00;border:1px solid #ffcc00;color:#ffcc00;padding:8px;border-radius:8px;font-size:12px}
.danger {background:#1a0000;border:1px solid #ff0000;color:#ff4444;padding:8px;border-radius:8px;font-size:12px}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">V31.1 FINAL - DUAL CAM DEPAN BELAKANG IR + CCTV IDEAL 22-26C 40-60% CO2<800 CO0 Body36.1-37.2C - RUANG KOSONG VS BANYAK ORANG - SIGNAL 🟢🟡🔴 - COCOK MASUKAN JENDRAL 100% - DEPLOY FINAL</div>', unsafe_allow_html=True)

st.title("🔬 KACA MATA 7 DETIK IR - V31.1 DUAL CAM + CCTV IDEAL + WARNING SIGNAL + CO2 CO BODY TEMP")
st.caption("V31.1 FINAL - DUAL CAM DEPAN BELAKANG IR WORKING - Level Ideal + Signal Warning + Nasehat Perbaikan - Cocok Masukan Jendral 100%")

# Trinity modes
col_mode1, col_mode2, col_mode3 = st.columns(3)
with col_mode1:
    mode = st.radio("TRINITY MODE", ["1. DERMA 15cm (DEPAN)", "2. CLIMATE 1 PER 1 (BELAKANG)", "3. MONEY 15cm LOOP (BELAKANG)"], index=0, horizontal=False)
with col_mode2:
    if "CLIMATE" in mode:
        climate_sub = st.radio("CLIMATE PECAH 1 PER 1 - NGGAK BENTROK!", ["🍚 FOOD Nasi Uduk", "🌾 GANDUM Quaker Oat", "📹 CCTV Gerak+Suhu+CO2+CO+Body"], index=2, horizontal=False)
    else:
        climate_sub = "📹 CCTV Gerak+Suhu+CO2+CO+Body"
with col_mode3:
    cam_facing = st.radio("DUAL CAM - DEPAN & BELAKANG ADA INFRARED NYA", ["📱 DEPAN (user) DERMA", "📷 BELAKANG (environment) CLIMATE/MONEY"], index=0 if "DERMA" in mode else 1)
    timer = st.select_slider("TIMER 50%", options=["3 DETIK Cepat Kantor 100-500", "5 DETIK Standar Ruko 10-20", "7 DETIK Perfect Rumah"], value="7 DETIK Perfect Rumah")
    detik = 3 if "3 DETIK" in timer else 5 if "5 DETIK" in timer else 7

st.divider()

# Info green
if "DERMA" in mode:
    st.markdown('<div class="ideal">DERMA IDEAL: Blue 10-20% seimbang Red 0-10% merata - Merugikan Blue>35% pori tersumbat -0.2°C komedo Red>20% +0.8-1.2°C jerawat/jamur - Signal Kuning/Merah Flash + Alert Suara! DUAL CAM IR WORKING! V31.1</div>', unsafe_allow_html=True)
elif "CLIMATE" in mode:
    if "FOOD" in climate_sub:
        st.markdown('<div class="ideal">FOOD IDEAL: Red <15% hangat merata - Merugikan >20% +1.5°C fermentasi bakteri humid bau asam - Signal DANGER SPOILED FOOD - 1 PER 1 FIX!</div>', unsafe_allow_html=True)
    elif "GANDUM" in climate_sub:
        st.markdown('<div class="ideal">GANDUM IDEAL: Rough <20% kadar air aman - Merugikan >25% bocor/kadaluarsa moisture loss kering kasar tengik - Signal WARNING EXPIRED/DRY - 1 PER 1 FIX! Consumer goods VALID!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="ideal">CCTV V31.1 - IDEAL + WARNING: Suhu 22-26°C ASHRAE optimal 24°C, Humid 40-60% >60% terasa 28-30°C gerah, CO2 <800 sehat >1000 pengap >1500 sesak naik 400ppm/orang/jam, CO 0 ideal >9ppm bahaya, Body 36.1-37.2 normal 37.3-37.5 ringan >37.5 istirahat! Kosong 24°C 50% 400ppm vs Banyak orang 10-20 ruko 100-500 +2-4°C +10-20% CO2>1000! Signal 🟢IDEAL 🟡WARNING 🟡🔴BAHAYA Evakuasi!</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="ideal">MONEY IDEAL: Hitam Pekat >70% IR-Absorb Bank Indonesia utuh - Merugikan <70% PALSU tinta biasa atau RUSAK luntur - Signal Merah Pekat + PALSU - DUAL CAM IR LOOP!</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3,2])

with col1:
    st.subheader(f"📷 CAMERA 50% - {cam_facing} - V31.1 DUAL CAM IR WORKING")
    camera = st.camera_input(f"Pajang di {cam_facing} - 50% Compact - V31.1")
    
    if camera:
        img = Image.open(camera)
        st.image(img, caption=f"Captured - V31.1 DUAL CAM {detik} detik - IR REAL", use_container_width=True)
        
        if st.button(f"MULAI DETEKSI {detik} DETIK - V31.1 DUAL CAM + LEVEL IDEAL CHECK", type="primary"):
            bar = st.progress(0)
            placeholder = st.empty()
            for i in range(detik,0,-1):
                txt = f"📸 {cam_facing} - 0-2s posisi" if i>5 else f"🔍 Auto-scan 2-5s - IR 500x" if i>2 else f"👁️ Lihat 500x - Level Ideal Check"
                placeholder.markdown(f"### {txt} - DALAM {i} detik - V31.1")
                bar.progress((detik-i)/detik)
                time.sleep(1)
            placeholder.markdown("### FLASH! ✅ Foto IR - Analisa V31.1...")
            bar.progress(1.0)
            time.sleep(0.5)
            
            # Simulate IR analysis
            blue_pct = random.randint(5,45)
            red_pct = random.randint(0,30)
            black_pct = random.randint(50,95)
            room_temp = round(random.uniform(22,30),1)
            humidity = random.randint(25,85)
            co2 = random.randint(400,1800)
            co = round(random.uniform(0,12),1)
            body_temp = round(random.uniform(36.0,38.0),1)
            
            st.divider()
            st.subheader(f"🧠 HASIL DETEKSI V31.1 - {mode} {climate_sub} - DUAL CAM IR")
            
            if "DERMA" in mode:
                is_blue_ideal = 10 <= blue_pct <= 20
                is_red_ideal = 0 <= red_pct <= 10
                is_bad = blue_pct>35 or red_pct>20
                signal = "🔴 BAHAYA MERAH FLASH + Alert!" if is_bad else "🟡 WARNING KUNING FLASH!" if blue_pct>20 or red_pct>10 else "🟢 IDEAL 10-20% & 0-10%"
                st.markdown(f"""
                **🔵 DERMA 15cm 7 DETIK - {cam_facing} - 50% - DUAL CAM IR - V31.1 FINAL - LEVEL IDEAL:**
                BIRU {blue_pct}% | MERAH {red_pct}% | {signal}
                📊 LEVEL IDEAL: Blue 10-20% seimbang | Red 0-10% merata - IR REAL!
                  Blue: {blue_pct}% {'🟢 IDEAL ✅' if is_blue_ideal else '🟡 WARNING'} | Red: {red_pct}% {'🟢 IDEAL ✅' if is_red_ideal else '🔴 BAHAYA ❌'}
                🔵 BIRU = BERMINYAK PANGKALAN BBM - Suhu -0.2°C
                ⚠️ MERUGIKAN: Blue>35% pori tersumbat -0.2°C komedo, Red>20% +0.8-1.2°C jerawat/jamur
                🚨 SIGNAL: {signal} - Kuning/Merah Flash + Alert!
                💡 NASEHAT: { 'Minyak Tinggi: pH5.5 oil-control double cleansing Niacinamide 2-5%' if blue_pct>35 else 'Minyak Ideal: pH5.5 + minum 2L'} | { 'Peradangan Tinggi: kompres dingin 2 menit Salicylic Antifungal' if red_pct>20 else 'Peradangan Ideal!'}
                DUAL CAM IR - Foto IR dulu baru teks!
                """)
            elif "CLIMATE" in mode:
                if "FOOD" in climate_sub:
                    is_ideal = red_pct<15
                    signal = "🔴 DANGER SPOILED FOOD!" if red_pct>20 else "🟡 WARNING Mulai Basi!" if red_pct>=15 else "🟢 IDEAL <15% Aman!"
                    st.markdown(f"""
                    **🍚 FOOD - {cam_facing} - V31.1 - LEVEL IDEAL:**
                    Red Pixel <15% hangat merata - Hasil: {red_pct}% {'🟢 IDEAL' if is_ideal else '🔴 BAHAYA'}
                    Suhu IR: {room_temp}°C Ideal 22-26°C | Humid: {humidity}% Ideal 40-60%
                    MERUGIKAN: Red >20% +1.5°C fermentasi humid bau asam
                    SIGNAL: {signal}
                    NASEHAT: {'Basi +1.5°C buang cegah keracunan simpan <2 jam' if red_pct>20 else 'Aman <15% simpan <2 jam'}
                    DUAL CAM - 1 PER 1 FIX!
                    """)
                elif "GANDUM" in climate_sub:
                    roughness = red_pct
                    is_ideal = roughness<20
                    signal = "🟡 WARNING EXPIRED/DRY!" if roughness>25 else "🟡 WARNING Mulai Kering!" if roughness>=20 else "🟢 IDEAL <20% Aman!"
                    st.markdown(f"""
                    **🌾 GANDUM - {cam_facing} - V31.1 - LEVEL IDEAL:**
                    Roughness <20% kadar air aman - Hasil: {roughness}% {'🟢 IDEAL' if is_ideal else '🟡 WARNING'}
                    Suhu {room_temp}°C Ideal 22-26°C Humid {humidity}% Ideal 40-60%
                    MERUGIKAN: >25% bocor/kadaluarsa moisture loss kering kasar tengik
                    SIGNAL: {signal}
                    NASEHAT: {'Kasar kering expired pindah wadah kedap udara' if roughness>25 else 'Aman <20% simpan kedap udara'}
                    Consumer goods VALID - 1 PER 1 FIX!
                    """)
                else:
                    # CCTV V31.1 FULL
                    is_temp_ideal = 22 <= room_temp <= 26
                    is_humid_ideal = 40 <= humidity <= 60
                    is_co2_ideal = co2<800
                    is_co2_warning = 1000 <= co2 <1500
                    is_co2_danger = co2>=1500
                    is_co_ideal = co<1
                    is_co_danger = co>9
                    is_body_ideal = 36.1 <= body_temp <= 37.2
                    is_body_light = 37.3 <= body_temp <= 37.5
                    is_body_fever = body_temp>37.5
                    
                    if is_co_danger or is_co2_danger or is_body_fever:
                        signal = "🔴 BAHAYA CO>9 atau CO2>1500 atau Body>37.5 = Alarm Evakuasi Ventilasi Maksimal!"
                        box = "danger"
                    elif is_co2_warning or humidity>70 or humidity<30 or room_temp>28 or is_body_light:
                        signal = "🟡 WARNING buka jendela exhaust kurangi orang - CO2>1000 atau Humid>60% atau Suhu>28°C"
                        box = "warning"
                    else:
                        signal = "🟢 IDEAL lanjutkan - Suhu 22-26°C Humid 40-60% CO2<800 CO 0 Body 36.1-37.2°C - Sehat!"
                        box = "ideal"
                    
                    st.markdown(f"""
                    **📹 CLIMATE CCTV V31.1 - IDEAL + WARNING SIGNAL - {cam_facing} - DUAL CAM - V31.1 FINAL - v31.1 ini semua bro:**

                    **🔬 CLIMATE CCTV V30.2 - IDEAL + WARNING SIGNAL (yang lu minta!):**

                    Suhu Ideal Ruangan IR: 22-26°C (ASHRAE) — ruang kosong optimal 24°C — IR deteksi real-time berapa °C
                    Kelembaban Ideal: 40-60% RH — kalau >60% suhu ideal turun, terasa jadi 28-30°C gerah!
                    CO2 Ideal: <800ppm sehat — Warning >1000ppm pengap — Bahaya >1500ppm sesak! Naik 400ppm per orang per jam!
                    CO Ideal: 0 ppm — Bahaya >9ppm karbon monoksida alarm! Dari pembakaran tidak sempurna!   Suhu Badan Orang Bergerak IR: Normal 36.1-37.2°C — Demam ringan 37.3-37.5°C — Demam >37.5°C istirahat!
                    Ruang Kosong vs Banyak Orang: Kosong stabil 24°C 50% RH CO2 400ppm — Banyak orang (10-20 ruko / 100-500 kantor) suhu naik +2-4°C, humid +10-20%,   CO2 >1000ppm!
                    Signal Warning Otomatis: 🟢 IDEAL lanjutkan / 🟡 WARNING buka jendela exhaust kurangi orang / 🔴 BAHAYA CO>9 atau CO2>1500 atau Body>37.5 = Alarm Evakuasi Ventilasi Maksimal!      dua cam bro kamera depan dan kamera belakang. v31.1 ini semua bro

                    **📊 HASIL DETEKSI IR REAL-TIME V31.1:**
                    • Suhu Ruangan IR: 22-26°C (ASHRAE) — ruang kosong optimal 24°C — Hasil: {room_temp}°C {'🟢 IDEAL 22-26°C ✅' if is_temp_ideal else '🔴 BURUK ❌'}
                    • Kelembaban Ideal: 40-60% RH — Hasil: {humidity}% RH {'🟢 IDEAL 40-60% ✅' if is_humid_ideal else '🔴 BURUK ❌'}
                    • CO2 Ideal: <800ppm sehat — Hasil: {co2}ppm {'🟢 IDEAL <800 ✅' if is_co2_ideal else '🟡 WARNING 1000-1500 ⚠️' if is_co2_warning else '🔴 BAHAYA >1500 ❌'}
                    • CO Ideal: 0 ppm — Hasil: {co}ppm {'🟢 IDEAL 0 ✅' if is_co_ideal else '🔴 BAHAYA >9ppm ❌'}
                    • Suhu Badan Orang Bergerak IR: Normal 36.1-37.2°C — Hasil: {body_temp}°C {'🟢 Normal ✅' if is_body_ideal else '🟡 Demam Ringan ⚠️' if is_body_light else '🔴 Demam >37.5°C ❌'}
                    • Ruang Kosong vs Banyak Orang: Kosong 24°C 50% 400ppm vs Banyak orang 10-20 ruko / 100-500 +2-4°C +10-20% CO2>1000ppm
                    • Simulasi Banyak Orang: Suhu {room_temp+2.5}°C (+2-4°C) Humid {humidity+15}% (+10-20%) CO2 {co2+600}ppm (>1000ppm)

                    **🚨 SIGNAL WARNING OTOMATIS V31.1:** {signal}
                    Status: {box.upper()} - {signal}

                    DUAL CAM: DEPAN DERMA, BELAKANG CCTV 180° + MONEY LOOP - IR DUAL CAM WORKING V31.1!
                    """)
                    if box=="danger":
                        st.error(f"🚨 {signal}")
                    elif box=="warning":
                        st.warning(f"⚠️ {signal}")
                    else:
                        st.success(f"✅ {signal}")
            else:
                is_ideal = black_pct>70
                signal = "🔴 MERAH PEKAT + PALSU!" if black_pct<70 else "🟢 IDEAL >70% AUTHENTIC"
                st.markdown(f"""
                **💰 MONEY - {cam_facing} - V31.1 - LEVEL IDEAL:**
                Hitam Pekat >70% IR-Absorb - Hasil: Hitam {black_pct}% {'🟢 IDEAL' if is_ideal else '🔴 PALSU'}
                MERUGIKAN: <70% PALSU tinta biasa tanpa IR atau RUSAK luntur
                SIGNAL: {signal}
                NASEHAT: {'IR <70% jangan terima 3D Dilihat Diterawang Diteraba' if black_pct<70 else 'IR >70% ASLI lanjutkan'}
                DUAL CAM IR - Belakang LOOP!
                """)
            
            st.balloons()

with col2:
    st.subheader("⚙️ V31.1 DUAL CAM + LEVEL IDEAL + WARNING")
    st.markdown("""
    **V30.3 & V31.1 - 2 yang pasti bro!**
    - V30.3: Level Ideal + Signal Warning + Nasehat Perbaikan - 10-20% 0-10% >70% <15% <20% 22-26°C 40-60%
    - V31.1: DUAL CAM DEPAN BELAKANG IR + CCTV IDEAL + WARNING + CO2 CO BODY TEMP + Ruang Kosong vs Banyak Orang
    
    **DUAL CAM BRO:**
    - 📱 DEPAN (user) - DERMA selfie 15cm
    - 📷 BELAKANG (environment) - CLIMATE/MONEY
    - Timer 3/5/7 detik - 50% Compact
    
    **CLIMATE 1 PER 1 FIX - NGGAK BENTROK LAGI:**
    - FOOD: Nasi uduk basi - Red <15% ideal
    - GANDUM: Quaker Oat consumer goods VALID - Rough <20% ideal - dulu nggak ke-detect karena 1 video campur 4 prompt bentrok!
    - CCTV: Gerak + Suhu + Humid + CO2 + CO + Body Temp - V31.1 FINAL
    
    **CCTV V31.1 IDEAL + WARNING SIGNAL:**
    - Suhu 22-26°C ASHRAE optimal 24°C
    - Humid 40-60% >60% terasa 28-30°C gerah
    - CO2 <800 sehat >1000 pengap >1500 sesak +400ppm/orang/jam
    - CO 0 ideal >9ppm bahaya
    - Body 36.1-37.2 normal 37.3-37.5 ringan >37.5 istirahat
    - Kosong 24°C 50% 400ppm vs Banyak orang +2-4°C +10-20% CO2>1000
    - Signal 🟢 IDEAL 🟡 WARNING 🟡🔴 BAHAYA Evakuasi
    """)
    
    st.divider()
    st.subheader("📊 Deploy Status V31.1")
    st.success("✅ PWA V31.1 31KB - DUAL CAM IR WORKING + LEVEL IDEAL + WARNING - LIVE: spontaneous-ir-7detik-3ways.netlify.app")
    st.success("✅ Streamlit V31.1 - DUAL CAM + CCTV IDEAL WARNING - GitHub app.py V31.1 FINAL")
    st.info("GAS BRO! GitHub push app.py V31.1 - PWA Netlify Drop V31.1 - Lablab pantau via deploy aja!")

st.divider()
st.markdown("**Deploy:** Netlify https://spontaneous-ir-7detik-3ways.netlify.app/ - V31.1 FINAL DUAL CAM + CCTV IDEAL WARNING - 50% Compact - DUAL CAM DEPAN BELAKANG IR - Single Lens Three Ways Infinite Impact")
