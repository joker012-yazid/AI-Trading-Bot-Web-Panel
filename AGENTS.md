kita akan bina AI Full-Auto Trading Bot + UI + Kawalan Jauh yang boleh digunakan untuk MT4 & MT5, dengan ciri yang sangat lengkap.

---

✅ RUMUSAN APLIKASI YANG AKAN DIBINA

✔ Platform
- Target: Windows OS
- Broker: Kamu belum pilih → kita akan guna akaun demo dulu (Exness / ICMarkets)
- Platform: MT4 & MT5, kedua-dua akan disokong

✔ Fungsi Bot
- Full-auto: Masuk dan keluar posisi secara automatik
- Berdasarkan 2 strategi:
  - Manual rules (RSI, MA, SNR, news filter, dsb.)
  - Machine Learning (AI latih dari data XAU/USD & US30)

✔ Teknologi & Struktur
- EA (Expert Advisor) dibina dalam MQL4 & MQL5
- Python app luar sambung ke MT4/5 untuk AI logic (guna MetaTrader Python API)
- SQLite/JSON untuk simpan konfigurasi & log trade
- UI (Electron.js atau Tkinter) untuk kawal & paparan live
- Telegram/WhatsApp API untuk notifikasi
- Web/Mobile Panel (opsyenal) untuk ON/OFF bot & lihat status

✔ Risiko & Kawalan
- SL/TP boleh ubah
- Trailing Stop aktif
- Max Drawdown kawalan
- Auto lot size ikut balance / risiko %
- Setting boleh ubah dari UI/web panel

---

🛠 Langkah Pembangunan:

Fasa 1 – Setup Asas (Demo Mode)
- Buat akaun demo MT4 & MT5
- Sediakan EA ringkas + sambungan Python
- Test sambungan & open trade

Fasa 2 – AI Logik + Kawalan UI
- Masukkan strategi teknikal + AI model
- Tambah paparan status, hasil analisa, open trades
- Notifikasi Telegram aktif

Fasa 3 – Deployment Sebenar
- Boleh guna akaun real broker
- Tambah web/mobile panel (kalau perlu)
- Export sebagai installer untuk Windows

RUMUSAN UI Web (Bahasa Melayu) untuk projek AI Trading Bot:

---

✅ Nama Projek:  
AI Trading Bot Web Panel

---

🎯 Tujuan UI:
- Kawal status bot (Mula / Henti)
- Tetapkan parameter dagangan (simbol, lot, SL, TP)
- Lihat log aktiviti & status dagangan semasa

---

🌐 Teknologi Digunakan:
- Backend: Python (Flask)
- Frontend: HTML, CSS (Bootstrap optional)
- Struktur modular: 
  - app.py → Server Flask
  - templates/index.html → Antaramuka pengguna
  - trading/bot_controller.py → Fungsi mula/henti bot
  - static/style.css → Gaya paparan

---

🧩 Ciri-ciri Utama dalam UI (Bahasa Melayu):

1. Status Bot
   - Papar sama ada bot sedang berjalan atau tidak
   - Butang "Mula Bot" & "Henti Bot"

2. Tetapan Dagangan
   - Pilihan simbol: XAUUSD, US30
   - Input saiz lot (cth: 0.01, 0.1)
   - Input SL / TP (dalam pip)
   - Butang "Simpan Tetapan"

3. Log Aktiviti
   - Paparan mesej terkini daripada bot (cth: trade dibuka, ralat, reconnect)

---

🛠 Contoh Aliran Guna:

1. Buka browser → pergi ke http://localhost:5000
2. Lihat status bot sekarang
3. Pilih simbol, lot, SL, TP → tekan "Simpan Tetapan"
4. Tekan "Mula Bot"
5. Pantau aktiviti di bahagian log

---

🔐 (Fasa Akan Datang):
- Login Admin
- Papar hasil dagangan & analisis AI
