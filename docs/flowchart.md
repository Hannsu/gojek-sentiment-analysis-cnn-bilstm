# Flowchart Proyek: Sentiment Analysis Gojek App Reviews
 1. Flowchart WAJIB (Alur Utama)

```mermaid
flowchart TD
    A[Input: Dataset Gojek Reviews - Kaggle] --> B[Preprocessing:
    Cleaning, Case Folding, Tokenisasi,
    Stopword Removal, Stemming]
    B --> C[Data Splitting:
    Train / Validation / Test]
    C --> D[Feature Extraction:
    Tokenizer + Padding]
    D --> E1[Training Model 1: CNN]
    D --> E2[Training Model 2: Hybrid CNN-BiLSTM]
    E1 --> F[Evaluasi Model 1:
    Accuracy, Precision, Recall, F1]
    E2 --> G[Evaluasi Model 2:
    Accuracy, Precision, Recall, F1]
    F --> H{Perbandingan Model 1 vs Model 2}
    G --> H
    H --> I[Pilih Model Terbaik
    berdasarkan F1-score]
    I --> J[Simpan Model Terbaik]
    J --> K[Backend API - FastAPI]
    K --> L[GUI Web - Streamlit]
    L --> M[Output: Prediksi Sentimen
    Positif / Netral / Negatif]
```
 2. Flowchart TAMBAHAN (Sunnah - Proses Ekstra)

```mermaid
flowchart TD
    A2[Data hasil preprocessing] --> B2{Distribusi kelas seimbang?}
    B2 -->|Tidak seimbang| C2[Imbalance Handling:
    Class Weighting]
    B2 -->|Seimbang| D2[Lanjut ke tahap berikutnya]
    C2 --> D2
    D2 --> E2[Simpan histori prediksi
    ke Database SQLite]
    E2 --> F2[Tampilkan riwayat prediksi
    di GUI Web]
```
 3. Keterangan Tambahan
- Proses **imbalance handling** dilakukan lewat `class_weight` pada saat training (lihat `notebooks/features.py`).
- Proses **database** dipakai untuk menyimpan histori setiap prediksi yang dilakukan lewat GUI (lihat `backend/app/core/database.py`).
- Ekstraksi fitur lanjutan (PCA/Chi-Square) bisa ditambahkan sebagai eksperimen tambahan jika ingin membandingkan representasi TF-IDF vs Embedding.
