# UAS - Sentiment Analysis Gojek App Reviews

Proyek klasifikasi sentimen ulasan aplikasi Gojek, mengembangkan referensi
jurnal CNN-only dengan menambahkan Model 2: **Hybrid CNN-BiLSTM**.

## Cara Menjalankan

### 1. Setup environment
```bash
pip install -r backend/requirements.txt
```

### 2. Pakai dataset asli
Download dari Kaggle: https://www.kaggle.com/datasets/ucupsedaya/gojek-app-reviews-bahasa-indonesia
Simpan sebagai `data/gojek_reviews.csv`.

### 3. Jalankan preprocessing & training
```bash
cd notebooks
python3 preprocessing.py
python3 train_and_evaluate.py
```
Hasil: model terbaik otomatis tersimpan di folder `models/`.

### 4. Jalankan backend API
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```
Dokumentasi API: http://localhost:8000/docs

### 5. Jalankan Aplikasi Mobile
Install `GojekReviewClassifier.apk` pada perangkat Android, atau build ulang dari source Flutter dan sesuaikan base URL backend pada konfigurasi service.

## Fitur
- Preprocessing teks Bahasa Indonesia (Sastrawi: stemming + stopword removal)
- Data splitting stratified (train/val/test)
- 2 model deep learning: CNN (non-hybrid) vs Hybrid CNN-BiLSTM
- Evaluasi lengkap: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Pemilihan model terbaik otomatis
- Imbalance handling (class weighting)
- Backend REST API (FastAPI) dengan database SQLite untuk histori prediksi
- Aplikasi mobile (Flutter) untuk analisis sentimen secara real-time
- Siap deploy ke platform hosting (Procfile disediakan)

## Struktur Proyek
- `backend/` — REST API (FastAPI), preprocessing, model service, dan database
- `data/` — dataset mentah dan hasil pembagian data (train/val/test)
- `hasil/` — hasil evaluasi model (grafik training, confusion matrix, ringkasan performa)
- `models/` — model terlatih beserta tokenizer dan label encoder
- `notebooks/` — script preprocessing, definisi arsitektur, training & evaluasi
- `GojekReviewClassifier.apk` — aplikasi mobile siap install

## Referensi
- Jurnal: Anissa, C. R., Tania, K. D., & Sari, W. K. (2025). *Sentiment Analysis on Google Play Store Reviews to Measure User Perception of the Gojek Application Using CNN*. Journal of Applied Informatics and Computing (JAIC), 9(6), 3322–3328.
- Dataset: Kaggle - ucupsedaya/gojek-app-reviews-bahasa-indonesia
- Struktur proyek terinspirasi dari repo kelompok: github.com/Reyysusanto/loan-approval