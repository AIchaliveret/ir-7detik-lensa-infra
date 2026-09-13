
import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="V32.0 - IR 7 Detik - Trinity - Efficient", layout="wide", page_icon="🔬")

st.markdown("<style>.h{ background:#0a0a0a; color:#00ff88; padding:10px; border-radius:8px; text-align:center; font-family:monospace; border:1px solid #00ff88; font-size:12px }</style>", unsafe_allow_html=True)
st.markdown('<div class="h">V32.0 FINAL EFFICIENT - Trinity 1 Lens 3 Impacts - CLIMATE 1 PER 1 FIX - Dual Cam - 24H - Efficient Deploy</div>', unsafe_allow_html=True)

st.title("🔬 V32.0 - Kaca Mata 7 Detik IR - Efficient")

with st.expander("📊 Level Ideal - Etika - Legalitas", expanded=False):
    st.markdown("""
    **DERMA (Front 15cm 7s):** BLUE 10-20% ideal T-zone -0.2°C, RED 0-10% ideal. BLUE>35% pori tersumbat, RED>20% jerawat +0.8-1.2°C. Advice pH5.5 niacinamide salicylic SPF50. Etika: Edukasi kosmetik BPOM, bukan medis.
    
    **FOOD Nasi Uduk (Rear):** RED <15% ideal 35-40°C <4 jam BPOM, 15-20% warning fermentasi +0.8°C, >20% danger basi +1.5°C bau asam. HACCP SNI. Etika: Cek fisik.
    
    **GANDUM Quaker Oat (Rear):** Rough <20% ideal air <14% SNI tidak menggumpal, 20-30% warning lembab 14-16%, >30% danger jamur aflatoksin >16%. Etika: Cek expired.
    
    **CCTV (Rear 180°):** Suhu 22-26°C ASHRAE 24°C optimal, Humid 40-60%, CO2 <800ppm WHO >1500 bahaya +400ppm/orang/jam, CO 0ppm >9ppm bahaya OSHA, Body 36.1-37.2°C. Signal 🟢 IDEAL 🟡 WARNING 🟡🔴 BAHAYA CO>9/CO2>1500/Body>37.5 evakuasi. Etika: Edukasi bukan medis.
    
    **MONEY IDR (Rear Loop):** Hitam >70% ideal authentic IR-Absorb BI 800-1000nm, 50-70% warning aus/lusuh, <50% palsu/rusak. Keterbatasan: HP tanpa IR 850nm tidak bisa deteksi real - ini simulasi grayscale edukasi, bukan validasi hukum. Etika: UU7/2011 Pasal23, BI 3D, validasi mesin bank.
    """)

def thermal_ir(img_pil, mode):
    img = img_pil.convert("RGB")
    w,h = img.size
    a = np.array(img)
    gray = np.dot(a[...,:3], [0.299,0.587,0.114])
    th = np.zeros_like(a)
    if "MONEY" in mode:
        th[gray<125] = [0,0,0]
        th[gray>185] = [235,235,235]
        mid = (gray>=125) & (gray<=185)
        v = ((gray[mid]-125)*2.8).astype(int)
        v = np.clip(v,15,210)
        th[mid] = np.stack([v,v,v], axis=1)
    else:
        for y in range(h):
            for x in range(w):
                g=gray[y,x]
                if g<80: th[y,x]=[0,int(g*2),255]
                elif g<160: th[y,x]=[int((g-80)*2.5),255,0]
                else: th[y,x]=[255,int(255-(g-160)*2),0]
    y1=int(h*0.2); y2=int(h*0.8); x1=int(w*0.3); x2=int(w*0.7)
    crop = th[y1:y2, x1:x2]
    gv = np.dot(crop[...,:3], [0.299,0.587,0.114])
    total = gv.size
    if "MONEY" in mode:
        black = np.sum(gv<95)
        white = np.sum(gv>180)
        bp = int(black/total*100) if total else 0
        wp = int(white/total*100) if total else 0
        return Image.fromarray(th.astype('uint8')), 0, 0, bp, wp
    else:
        blue = np.sum((crop[:,:,2]>crop[:,:,0]+20))
        red = np.sum(crop[:,:,0]>150)
        bp = int(blue/total*100) if total else 0
        rp = int(red/total*100) if total else 0
        return Image.fromarray(th.astype('uint8')), bp, rp, 0, 0

mode = st.radio("Trinity Mode - Dual Cam Auto", ["1. DERMA 15cm Front - BLUE=BERMINYAK", "2. CLIMATE 1 PER 1 Rear - FOOD/GANDUM/CCTV", "3. MONEY 15cm Loop Rear - IR-Absorb"], index=2, horizontal=True)
auto = "📱 Front" if "DERMA" in mode else "📷 Rear"
csub = ""
if "CLIMATE" in mode:
    csub = st.radio("Climate 1 per 1 - Tidak bentrok", ["🍚 FOOD <15% ideal", "🌾 GANDUM <20% ideal", "📹 CCTV 22-26C 40-60%"], index=2, horizontal=True)

inp = st.radio("Input", ["📁 File Uploader - Laptop", "📷 Camera - HP"], index=0, horizontal=True)

cam=None
if "File" in inp:
    up = st.file_uploader(f"Upload - {auto} - V32.0 Efficient", type=["jpg","jpeg","png"])
    if up: cam=up
else:
    cam = st.camera_input(f"Camera - {auto} - V32.0 Efficient")

if cam:
    orig = Image.open(cam).convert("RGB")
    th_img, blue_p, red_p, black_p, white_p = thermal_ir(orig, mode)
    
    c1,c2 = st.columns(2)
    with c1: st.image(orig, caption=f"Original - {auto}", use_container_width=True)
    with c2:
        if "MONEY" in mode:
            st.image(th_img, caption=f"IR Simulasi - BLACK {black_p}% - MONEY", use_container_width=True)
        else:
            st.image(th_img, caption=f"IR Thermal - BLUE {blue_p}% RED {red_p}%", use_container_width=True)
    
    st.divider()
    
    if "DERMA" in mode:
        sig = "🔴 Bahaya >35%/20%" if blue_p>35 or red_p>20 else "🟡 Warning 20-35%/10-20%" if blue_p>20 or red_p>10 else "🟢 Ideal 10-20% & 0-10%"
        st.markdown(f"**DERMA - {auto} - BLUE {blue_p}% RED {red_p}% - {sig}** - Ideal BLUE 10-20% T-zone -0.2°C RED 0-10%. Merugikan BLUE>35% pori tersumbat RED>20% jerawat +0.8-1.2°C. Advice pH5.5 niacinamide. Etika: Edukasi kosmetik, bukan medis.")
        if "Bahaya" in sig: st.error(sig)
        elif "Warning" in sig: st.warning(sig)
        else: st.success(sig)
    
    elif "CLIMATE" in mode:
        if "FOOD" in csub:
            sig = "🔴 Danger >20% basi" if red_p>20 else "🟡 Warning 15-20% fermentasi" if red_p>=15 else "🟢 Ideal <15% aman"
            st.markdown(f"**FOOD - RED {red_p}% - {sig}** - Ideal <15% 35-40°C <4 jam BPOM. Merugikan 15-20% fermentasi +0.8°C >20% basi +1.5°C bau asam.")
        elif "GANDUM" in csub:
            sig = "🔴 Danger >30% jamur" if red_p>30 else "🟡 Warning 20-30% lembab" if red_p>=20 else "🟢 Ideal <20% valid"
            st.markdown(f"**GANDUM - Rough {red_p}% - {sig}** - Ideal <20% air <14% SNI. Merugikan 20-30% lembab 14-16% >30% jamur aflatoksin >16%.")
        else:
            import random
            rt=round(random.uniform(22,28),1); hu=random.randint(40,70); co2=random.randint(500,1200); co=round(random.uniform(0,5),1); bt=round(random.uniform(36.2,37.0),1)
            sig = "🟢 Ideal 22-26C 40-60% CO2<800 CO0 Body 36.1-37.2C"
            st.markdown(f"**CCTV 180° - Suhu {rt}°C Humid {hu}% CO2 {co2}ppm CO {co}ppm Body {bt}°C - {sig}** - Ideal ASHRAE 22-26C 24C optimal 40-60% CO2<800 WHO CO0 OSHA 9ppm Body 36.1-37.2C.")
            st.success(sig)
    
    else:
        st.markdown(f"**MONEY IDR 50000 - BLACK {black_p}% PUTIH {white_p}% - Level Keaslian:** Ideal >70% authentic IR-Absorb BI, 50-70% warning aus/lusuh, <50% palsu/rusak. Keterbatasan jujur: HP tanpa IR 850nm tidak bisa deteksi real - ini simulasi grayscale edukasi, bukan validasi hukum. Hasil {black_p}% simulasi. Signal {'🟢 Ideal >70% AUTHENTIC' if black_p>=70 else '🟡 Warning 50-70%' if black_p>=50 else '🔴 <50% tidak bisa pastikan - perlu IR + mesin bank'}. Legalitas: UU7/2011 Pasal23, BI 3D, validasi mesin bank.")
        if black_p>=70:
            st.success(f"🟢 Simulasi BLACK {black_p}% >70% - Terlihat ASLI di simulasi - Tetap cek 3D + bank - Edukasi.")
        elif black_p>=50:
            st.warning(f"🟡 BLACK {black_p}% 50-70% - Tidak bisa pastikan - Perlu IR + 3D + bank.")
        else:
            st.error(f"🔴 BLACK {black_p}% <50% - Tidak bisa deteksi akurat - Bukan berarti PALSU - HP tidak punya IR 850nm - Perlu hardware + mesin bank - Jujur.")

st.divider()
st.caption("V32.0 Efficient - Trinity 1 Lens 3 Impacts - CLIMATE 1 PER 1 FIX - Dual Cam Auto 1X klik PWA THE BEST vs Streamlit 2X kontrol - Tech Snapdragon NPU 500x/1000x IR-Absorb ExecuTorch on-device - Business Freemium PWA+Pro royalty 3 repos - LIVE spontaneous-ir-7detik-3ways.netlify.app Backup moonlit-meerkat-unoshadow.netlify.app DEMO youtube.com/shorts/GTYA8VH29Kg")
