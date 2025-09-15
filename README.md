markdown
🧠 AI Trading Bot (Versi Web UI - Bahasa Melayu)

Satu aplikasi *AI Trading Bot* yang boleh dikawal melalui *antara muka web*. Bot ini disambungkan ke platform *MT4/MT5*, dan membolehkan dagangan automatik untuk simbol seperti *XAU/USD* dan *US30*.

---

📌 Fungsi Utama

1. ✅ *Kawal Status Bot*
   - Mula atau henti bot dengan satu klik
   - Paparan status semasa

2. ⚙ *Tetapan Dagangan*
   - Pilih simbol: XAU/USD, US30
   - Tetapkan saiz lot, Stop Loss, Take Profit

3. 📋 *Log Aktiviti*
   - Lihat semua aktiviti bot: trade dibuka, status sambungan, ralat

---

🧱 Struktur Projek
```

AI_Trading_Bot_Web/
├── app.py                      # Aplikasi Flask utama
├── templates/
│   └── index.html              # Antaramuka pengguna
├── static/
│   └── style.css               # Gaya paparan
├── trading/
│   └── bot_controller.py       # Fungsi mula/henti bot
├── requirements.txt            # Pakej Python yang diperlukan
└── README.md                   # Dokumen ini
```

---

🖥 Keperluan Sistem

- Python 3.8+
- Flask
- (Pilihan) Pakej MetaTrader5 untuk sambungan sebenar
- MT4/MT5 dipasang di Windows

- Sambungan ke terminal MT5 (sedia log masuk akaun demo/real)

---

🔧 Cara Pasang & Jalankan

1. Pasang pakej keperluan asas:

bash
pip install -r requirements.txt


2. (Opsyenal) Pasang `MetaTrader5` jika mahu sambungan sebenar:

bash
pip install MetaTrader5


3. Jalankan server Flask:

bash
python app.py


4. Buka browser:


http://localhost:5000


---

🧠 Fungsi Akan Datang

- Panel login admin
- Analisis AI berdasarkan sejarah data
- Integrasi Telegram/WhatsApp untuk notifikasi
- Panel kawalan melalui telefon

---

📞 Sokongan

Sebarang soalan atau permintaan penambahan fungsi, sila hubungi pembangun atau guna antaramuka ini untuk sambung pembangunan.

---

Hak Cipta © 2025 - Projek AI Trading Bot
