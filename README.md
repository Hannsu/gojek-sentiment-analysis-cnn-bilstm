UAS - Sentiment Analysis Gojek App Reviews

Proyek klasifikasi sentimen ulasan aplikasi Gojek, mengembangkan referensi
jurnal CNN-only dengan menambahkan Model 2: **Hybrid CNN-BiLSTM**.

 Cara Menjalankan

1. Setup environment
```bash
pip install -r backend/requirements.txt
pip install -r gui_web/requirements.txt
```

2. (Opsional) Pakai dataset asli
Download dari Kaggle: https://www.kaggle.com/datasets/ucupsedaya/gojek-app-reviews-bahasa-indonesia
Simpan sebagai `data/gojek_reviews.csv`.

3. Jalankan preprocessing & training
```bash
cd notebooks
python3 preprocessing.py
python3 train_and_evaluate.py
```
Hasil: model terbaik otomatis tersimpan di folder `models/`.

4. Jalankan backend API
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```
Dokumentasi API: http://localhost:8000/docs

5. Jalankan GUI Web
```bash
cd gui_web
streamlit run app_streamlit.py
```

 Fitur
- Preprocessing teks Bahasa Indonesia (Sastrawi: stemming + stopword removal)
- Data splitting stratified (train/val/test)
- 2 model deep learning: CNN (non-hybrid) vs Hybrid CNN-BiLSTM
- Evaluasi lengkap: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Pemilihan model terbaik otomatis
- Imbalance handling (class weighting)
- Database SQLite untuk histori prediksi
- GUI Web interaktif (Streamlit)

 Dokumentasi
- Flowchart: `docs/flowchart.md`
- Laporan: `docs/laporan_ringkas.md`

 Referensi
- Jurnal: Sentiment Analysis on Google Play Store Reviews to Measure User
  Perception of the Gojek Application Using CNN (JAIC - Polibatam)
- Dataset: Kaggle - ucupsedaya/gojek-app-reviews-bahasa-indonesia
- Struktur proyek terinspirasi dari repo kelompok: github.com/Reyysusanto/loan-approval
