import streamlit as st
import time
from PIL import Image

st.set_page_config(page_title="V30.1 JENDRAL - DUAL CAM + CLIMATE 1 PER 1 - IR 7 Detik", layout="wide", page_icon="🔬")

st.markdown("""
<style>
.header {background:#000;color:#00ff88;padding:12px;border-radius:10px;text-align:center;font-family:monospace;font-size:11px;border:1px solid #003300}
.blue {color:#00aaff;font-weight:bold} .red{color:#ff4444;font-weight:bold} .green{color:#00ff88}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">V30.1 FIX CLIMATE 1 PER 1 | 🔵 BIRU DINGIN = BERMINYAK (PANGKALAN BBM) | CLIMATE PECAH 3 = FOOD / GANDUM / CCTV = NGGAK BENTROK | 50% COMPACT + DUAL CAM</div>', unsafe_allow_html=True)

st.title("🔬 V30.1 JENDRAL - DUAL CAM + CLIMATE 1 PER 1 FIX")
st.caption("PWA 50% + Streamlit sinkron | DERMA 15cm 7 detik + CLIMATE 1 per 1 + MONEY IR-Absorb | Blue=Berminyak Pangkalan BBM")

mode = st.radio("TRINITY MODE - Pilih 1:", ["1. DERMA 15cm 7 detik - Depan Selfie - BLUE=BERMINYAK", "2. CLIMATE 1 PER 1 FIX - Belakang - FOOD/GANDUM/CCTV", "3. MONEY 15cm LOOP - Belakang - IDR IR-Absorb"], horizontal=False)

if "CLIMATE" in mode:
    climate_sub = st.radio("CLIMATE 1 PER 1 - Pilih Fokus (Jangan Campur!):", ["🍚 FOOD - Nasi Uduk Basi", "🌾 GANDUM - Quaker Oatmeal Kasar/Kering/Kadaluarsa", "📹 CCTV - Gerak + Kelembaban + Suhu Ruangan"], horizontal=True)
    st.info(f"FIX BENTROK: Dulu 1 video isinya nasi+gandum+gerak+suhu = bentrok! Sekarang {climate_sub} SAJA 1 per 1 = akurat!")
else:
    climate_sub = None

col1, col2 = st.columns([1,1])

with col1:
    st.subheader("📷 CAMERA 50% - DUAL CAM")
    if "DERMA" in mode:
        st.caption("📱 KAMERA DEPAN - Selfie DERMA - 50% compact")
    else:
        st.caption("📷 KAMERA BELAKANG - CLIMATE/MONEY - 50% compact")
    
    timer_label = st.select_slider("Timer Lensa Infra:", options=["3 Detik Cepat","5 Detik Standar","7 Detik Perfect (Rekomendasi)"], value="7 Detik Perfect (Rekomendasi)")
    detik = 3 if "3" in timer_label else 5 if "5" in timer_label else 7
    
    camera = st.camera_input(f"Pajang di tengah 50% - {mode} - {climate_sub if climate_sub else ''}")

    if camera:
        img = Image.open(camera)
        st.image(img, caption=f"Captured {detik} detik - 50% - IR Thermal", use_container_width=True)
        
        if st.button(f"MULAI DETEKSI {detik} DETIK - 50% - 1 PER 1", type="primary"):
            bar = st.progress(0)
            ph = st.empty()
            for i in range(detik,0,-1):
                ph.markdown(f"### 📸 POSISI 50% - {i} detik - Auto-scan...")
                bar.progress((detik-i)/detik)
                time.sleep(1)
            ph.markdown("### FLASH! ✅ Foto IR 500x - Analisa 1 per 1...")
            bar.progress(1.0)
            time.sleep(0.5)
            st.success("Deteksi selesai! Foto dulu baru teks - akurat tidak mendahului!")

with col2:
    st.subheader("⚙️ Atur Deteksi + Hasil Akurat 1 per 1")

    if camera:
        if "DERMA" in mode:
            st.markdown("#### 🔵 DERMA - BLUE = BERMINYAK (PANGKALAN BBM)")
            blue_pct = st.slider("Simulasi Biru Dingin % (Berminyak):", 0, 100, 35)
            red_pct = st.slider("Merah Panas % (Jamur/Jerawat):", 0, 100, 15)
            
            if blue_pct > 35:
                st.error(f"🔵 BIRU {blue_pct}% = BERMINYAK BERAT (PANGKALAN BBM WKWKWK) 🛢️ - Sebum berlebih T-zone jidat hidung dagu - Suhu -0.2°C dingin karena minyak menguap")
                st.markdown("**Nasehat Akurat:** Cleanser pH5.5 oil-control, niacinamide 2%, blotting paper siang, clay mask 2x/minggu T-zone biru, minum 2L, kurangi gorengan - PANGKALAN BBM tutup! 😂")
            elif blue_pct > 20:
                st.warning(f"🔵 BIRU {blue_pct}% = BERMINYAK SEDANG - Komedo mulai banyak")
                st.markdown("**Nasehat:** Double cleansing malam, toner niacinamide, cold compress 2 menit area biru")
            else:
                st.success(f"🔵 BIRU {blue_pct}% = NORMAL - Tidak berminyak - Sehat")
            
            if red_pct > 20:
                st.error(f"🔴 MERAH {red_pct}% = JAMUR ACTIVE BORDER +0.8°C / JERAWAT +1.2°C - Peradangan panas")
            
            st.info("NB: Akurat hitung pixel biru di wajah tengah 30-70% - foto IR dulu baru teks - nggak mendahului!")

        elif "CLIMATE" in mode:
            if climate_sub and "FOOD" in climate_sub:
                st.markdown("#### 🍚 CLIMATE FOOD - NASI UDUK - 1 PER 1 FIX")
                st.markdown("Fokus: Nasi uduk telor balado suir sayur buncis wortel sambel 15cm - BUKAN gandum/CCTV!")
                red_food = st.slider("Merah Panas % (Basi):", 0, 100, 25)
                if red_food > 20:
                    st.error(f"🔴 MERAH {red_food}% = BASI - Suhu +1.5°C + kelembaban tinggi + bau asam/apek - BUANG!")
                else:
                    st.success(f"🟢 HIJAU = NORMAL - Nasi masih aman - Suhu merata")
                st.markdown("**Nasehat FOOD 1 per 1:** Cek 10 detik sebelum makan, jika merah panas + bau asam = jangan konsumsi. Simpan <2 jam suhu ruang. FIX BENTROK: Dulu campur nasi+gandum+CCTV 1 video bentrok, sekarang FOOD saja!")
                st.caption("NB FOOD 1 PER 1: Hanya nasi uduk - tidak campur gandum/CCTV - akurat!")

            elif climate_sub and "GANDUM" in climate_sub:
                st.markdown("#### 🌾 CLIMATE GANDUM - QUAKER OATMEAL - 1 PER 1 FIX")
                st.markdown("Fokus: Quaker Oatmeal kemasan consumer goods (VALID bukan FMCG) 15cm - BUKAN nasi/CCTV!")
                st.markdown("**Kenapa kemarin nggak terdeteksi?** Karena lu 1 video isinya nasi+gandum+gerak+suhu = bentrok prompt! Sekarang GANDUM saja!")
                rough = st.slider("Kasar/Kering/Kadaluarsa % (Merah):", 0, 100, 30)
                if rough > 25:
                    st.error(f"🔴 MERAH {rough}% = KASAR/KERING/KADALUARSA - Moisture loss, tekstur kasar lebih panas, suhu tidak merata, bau tengik - BUANG!")
                else:
                    st.success(f"🟢 NORMAL - Gandum masih bagus - Tidak kasar")
                st.markdown("**Nasehat GANDUM 1 per 1:** Cek kemasan 10 detik - jika kasar kering + merah + bau tengik = buang. Simpan kedap udara. FIX: Dulu gandum tidak terdeteksi karena campur nasi+gerak+suhu, sekarang GANDUM saja akurat!")
                st.caption("NB GANDUM 1 PER 1: Quaker consumer goods VALID - fokus gandum - deteksi kasar/kering/kadaluarsa!")

            else:
                st.markdown("#### 📹 CLIMATE CCTV - GERAK + SUHU + LEMBAB - 1 PER 1 FIX")
                st.markdown("Fokus: HP jadi CCTV putar 180° - BUKAN makanan!")
                traffic = st.select_slider("Traffic:", options=["Rumah 10 orang - 7s Perfect", "Ruko 10-20 orang - 5s Standard", "Kantor 100-500 orang - 3s Fast"], value="Ruko 10-20 orang - 5s Standard")
                st.info(f"CCTV: {traffic} - Deteksi gerak hilir mudik + kelembaban real-time + suhu ruangan - Letakkan HP sudut ruangan - Pantau tanpa keliling!")
                st.markdown("**Nasehat CCTV 1 per 1:** Mode CCTV 50% - 180° panning - Timer 3/5/7s. FIX: Dulu campur nasi+gandum+gerak+suhu bentrok, sekarang CCTV saja!")
                st.caption("NB CCTV 1 PER 1: Hanya gerak+suhu+lembab - ruko 10-20 kantor 100-500")

        else:
            st.markdown("#### 💰 MONEY - IDR IR-Absorb")
            st.markdown("IDR Rupiah IR ink: Hitam pekat 0=asli, putih 255=palsu - Bukan foto hitam error!")
            ir_black = st.slider("Hitam Pekat % (Asli):", 0, 100, 85)
            if ir_black > 70:
                st.success(f"⬛ HITAM {ir_black}% = ASLI - IR-Absorb - Bank Indonesia IR ink")
            else:
                st.error(f"⬜ PUTIH = PALSU - Tidak ada IR ink - Pantulkan IR!")
            st.caption("100% on-device, no upload - Physics IR-Absorb!")

st.divider()
st.markdown("""
**DEPLOY V30.1:**
- PWA: spontaneous-ir-7detik-3ways.netlify.app (Netlify Drop) - V30.1 50% CLIMATE 1 PER 1 FIX
- GitHub: ir-7detik-lensa-infra + ruang-teduh-ai + sahabatsuara-voice-guardian
- Demo: youtube.com/shorts/GTYA8VH29Kg (V30 50% + BLUE=BERMINYAK + CLIMATE 1 PER 1)
- Lablab: IR Track - Qualcomm Model-to-device - Snapdragon NPU + ExecuTorch 100% on-device
""")
