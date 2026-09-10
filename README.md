# IR Face Scanner - 7 Detik Lensa Infra Deteksi | Lablab.ai Competition

## Model: V5 WIDE SIMPLE - The Best Simple

**Deploy Live:** https://sage-gnome-459585.netlify.app/

### Apa itu?
Web/App full kamera dengan IR sebagai Lensa Pembesar Shortir untuk deteksi kesehatan kulit. 
- Full camera live FACE ID • IR frame
- Bottom sheet Lembaran Keterangan bisa sliding kebawah
- Klik MULAI DETEKSI -> slide down -> auto countdown 3/5/7 detik pajang wajah -> lensa auto-scan -> auto capture -> hasil analisa

### Kenapa 7 Detik Perfect untuk Promo IR?
0-2s atur posisi, 2-5s lensa IR auto-scan shortir wajah (thermal merah +0.8°C jamur, biru -0.2°C komedo), 5-7s user lihat detail pori/komedo/bulu di 500x/1000x VISUAL, baru FLASH capture. Bikin user betah, bukan filter instant.

### Kolom Atur Deteksi (Bisa Pilih):
- Group1: [Kulit Wajah Lembab, Kulit Wajah Kering]
- Group2: [Berpori Besar, Berkomedo, Berflek]
- Group3: [Bertungau Demodex, Berpanu Menjamur, Awas Bakteri & Virus -> Jerawat Bernanah]

### Bisakah IR deteksi bakteri & virus?
TIDAK LANGSUNG. Bakteri 0.5-1 mikron, virus 20-300nm lebih kecil dari pixel IR. IR hanya deteksi panas peradangan +0.6-1.5°C. Kepastian 100% butuh lab. Ini early warning.

### 8 Kriteria Deteksi Sistematis:
Lembab, Kering, Berpori Besar 0.3-0.6mm, Komedo, Berbulu Halus vellus, Berjamur Active border, Berminyak, Flek Hitam
Jika bersih: "KULIT ANDA PERFECT BERSIH ✨ 95/100"

### Saran Formula & Nasehat Dokter:
Sesuai kadar ingredien skincare, ikuti petunjuk dokter, reminder 07:00 & 21:00

### Tech:
- Frontend: Vanilla HTML/CSS/JS, getUserMedia, Canvas thermal, PWA Ready, Responsive split 50/50 fix anti hitam
- Backend (Streamlit): Python + OpenCV for IR simulation
- NPU: Snapdragon realtime (simulasi)

### Deploy:
1. Netlify: drag & drop index.html ke https://app.netlify.com/sites/sage-gnome-459585/deploys
2. Streamlit: streamlit run app.py

### Untuk Lablab.ai:
- Link Demo: https://sage-gnome-459585.netlify.app/ + Streamlit Cloud link
- GitHub: push index.html + app.py + requirements.txt
- Video: rekam flow 7 detik lensa infra

Made with ❤️ for healthy skin detection.
