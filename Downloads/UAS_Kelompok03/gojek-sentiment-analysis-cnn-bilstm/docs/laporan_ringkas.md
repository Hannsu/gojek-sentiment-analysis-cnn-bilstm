# Laporan Proyek: Sentiment Analysis Ulasan Aplikasi Gojek

## 1. Pendahuluan
Proyek ini merupakan pengembangan dari studi yang dilakukan pada jurnal
"Sentiment Analysis on Google Play Store Reviews to Measure User Perception
of the Gojek Application Using CNN" (JAIC, Polibatam), yang hanya menggunakan
1 model deep learning (CNN). Pada proyek ini ditambahkan model kedua, yaitu
**Hybrid CNN-BiLSTM**, sebagai pembanding untuk melihat apakah kombinasi
fitur lokal (CNN) dan konteks sekuensial (BiLSTM) mampu meningkatkan performa
klasifikasi sentimen.

## 2. Dataset
- Sumber: Kaggle - "Gojek App Reviews Bahasa Indonesia" (ucupsedaya)
- Jenis: Data teks mentah (raw data), bukan gambar
- Kolom asli: `userName`, `content`, `score`, `at`, `appVersion`
- **Jumlah data asli: 225.002 baris**
- **Jumlah data setelah preprocessing: 215.001 baris** (± 10.001 baris terbuang
  karena menjadi teks kosong setelah proses cleaning/stopword removal)
- Label: dihasilkan dari konversi rating (`score`) — rating 4-5 = positif,
  rating 3 = netral, rating 1-2 = negatif

### Distribusi Label (Data Asli)
| Label    | Jumlah  | Persentase |
|----------|---------|------------|
| Positif  | 151.640 | 70.53%     |
| Negatif  | 54.055  | 25.14%     |
| Netral   | 9.306   | 4.33%      |

> **Catatan penting**: Dataset ini mengalami **imbalance signifikan**, terutama
> pada kelas "netral" yang hanya berjumlah 4.33% dari keseluruhan data. Hal ini
> menjadi salah satu tantangan utama dalam klasifikasi dan berdampak langsung
> pada hasil evaluasi (lihat bagian Hasil & Pembahasan).

### Pembagian Data (Data Splitting)
| Split | Jumlah Baris | Positif | Negatif | Netral |
|-------|-------------|---------|---------|--------|
| Train (70%) | 150.500 | 106.148 | 37.838 | 6.514 |
| Validation (10%) | 21.500 | 15.164 | 5.405 | 931 |
| Test (20%) | 43.001 | 30.328 | 10.812 | 1.861 |

Split dilakukan secara **stratified** agar proporsi tiap kelas tetap terjaga
konsisten di ketiga subset data.

## 3. Metodologi
1. **Preprocessing**: cleaning teks, case folding, stopword removal, dan
   stemming menggunakan library Sastrawi.
2. **Data Splitting**: train/validation/test dengan stratifikasi kelas.
3. **Feature Extraction**: tokenisasi + padding sequence untuk input deep learning.
4. **Imbalance Handling**: class weighting saat training (fitur tambahan).
5. **Model 1 (non-hybrid)**: CNN — Embedding, Conv1D, MaxPooling, Dense.
6. **Model 2 (hybrid)**: CNN-BiLSTM — kombinasi Conv1D untuk fitur n-gram lokal
   dan BiLSTM untuk menangkap konteks sekuensial dua arah.
7. **Evaluasi**: Accuracy, Precision, Recall, F1-score (macro average), dan
   Confusion Matrix.
8. **Pemilihan model terbaik**: berdasarkan F1-score tertinggi pada data test.
9. **Deployment**: model terbaik di-serve melalui backend FastAPI dan
   diakses lewat GUI Web (Streamlit).

## 4. Hasil Training (Grafik Akurasi & Loss)
Grafik dihasilkan otomatis oleh `notebooks/train_and_evaluate.py` dan
tersimpan di `docs/hasil/`:
- `training_history_Model1_CNN.png`
- `training_history_Model2_CNN_BiLSTM_Hybrid.png`

*(Tempelkan gambar ini di laporan Word/PDF final sebagai lampiran "Hasil Training")*

## 5. Hasil Testing (Confusion Matrix & Hasil Prediksi)
- Confusion matrix (gambar): `docs/hasil/confusion_matrix_Model1_CNN.png` dan
  `docs/hasil/confusion_matrix_Model2_CNN_BiLSTM_Hybrid.png`
- Contoh hasil prediksi pada data test: `docs/hasil/sample_predictions.csv`
  (berisi teks asli, label aktual, dan label hasil prediksi model terbaik)

## 6. Tabel Perbandingan Model (Hasil Aktual - Dataset Asli Kaggle)

| Model | Accuracy | Precision | Recall | F1-score |
|-------|----------|-----------|--------|----------|
| Model 1 - CNN | 0.8225 | 0.6082 | 0.6289 | 0.6089 |
| **Model 2 - Hybrid CNN-BiLSTM** | **0.8300** | **0.6171** | **0.6457** | **0.6209** |

**Model terbaik yang dipilih otomatis oleh sistem: Model 2 (Hybrid CNN-BiLSTM)**,
berdasarkan F1-score tertinggi (0.6209 vs 0.6089).

### Pembahasan

**1. Hybrid CNN-BiLSTM konsisten unggul di semua metrik.**
Penambahan layer BiLSTM di atas fitur lokal yang diekstrak CNN terbukti
membantu model menangkap konteks sekuensial dan hubungan antar kata dalam
kalimat ulasan dengan lebih baik dibanding CNN murni, meski peningkatannya
tergolong tipis (~1% pada F1-score).

**2. Kesenjangan antara Accuracy (~82-83%) dan F1-score (~61%) menunjukkan
dampak nyata dari imbalance data.**
Dataset memiliki distribusi label yang sangat timpang: kelas "positif"
mendominasi 70.53% data, sementara kelas "netral" hanya 4.33%. Accuracy yang
terlihat tinggi sebagian besar didorong oleh keberhasilan model menebak kelas
mayoritas (positif), sementara performa pada kelas minoritas (terutama netral)
jauh lebih rendah — inilah yang tercermin pada F1-score macro-average yang
jauh lebih rendah dari accuracy.

**3. Class weighting membantu tapi tidak sepenuhnya mengatasi imbalance.**
Meski sudah diterapkan `class_weight="balanced"` saat training, jumlah data
kelas netral (hanya 9.306 dari 215.001 baris) tetap menjadi tantangan besar.
Ini adalah temuan penting yang bisa dijadikan bahan diskusi/rekomendasi
pengembangan lebih lanjut (misalnya oversampling SMOTE khusus kelas netral,
atau menggabungkan kelas netral+negatif jika konteks bisnis memungkinkan).

**4. Ukuran dataset yang besar (215rb baris) memberikan hasil yang lebih
andal dan representatif** dibanding pengujian pada data sampel kecil,
sehingga angka evaluasi ini layak dijadikan dasar kesimpulan akademik.

## 7. Link GitHub
Cantumkan link repository GitHub kelompok yang berisi seluruh source code
program Python final di sini: `https://github.com/<username>/<repo-kelompok>`

## 8. Kesimpulan
- Pipeline end-to-end (preprocessing -> splitting -> training -> evaluasi ->
  pemilihan model -> deployment GUI) berhasil diimplementasikan dan diuji
  pada dataset asli Gojek App Reviews (225.002 baris data mentah).
- Dari dua model deep learning yang dibandingkan, **Hybrid CNN-BiLSTM**
  terbukti unggul di seluruh metrik evaluasi (Accuracy 0.8300, Precision
  0.6171, Recall 0.6457, F1-score 0.6209) dibandingkan CNN non-hybrid
  (Accuracy 0.8225, F1-score 0.6089), sehingga dipilih sebagai model terbaik
  untuk diimplementasikan pada GUI.
- Ditemukan tantangan **imbalance data** yang signifikan pada dataset,
  khususnya kelas "netral" yang hanya berjumlah 4.33% dari total data,
  menyebabkan kesenjangan antara accuracy dan F1-score. Ini menjadi catatan
  penting untuk pengembangan model di masa depan.
- Model terbaik telah berhasil diintegrasikan ke backend FastAPI dan GUI Web
  (Streamlit) sehingga dapat digunakan secara langsung oleh pengguna akhir
  untuk menganalisis sentimen ulasan baru secara real-time.

## 9. Struktur Proyek
```
UAS_KelompokXXX/
├── data/                # dataset asli & hasil preprocessing
├── notebooks/           # preprocessing, feature extraction, model, training
├── models/              # model terbaik + tokenizer + label encoder tersimpan
├── backend/             # FastAPI (API prediksi + database histori)
├── gui_web/             # GUI Web (Streamlit)
└── docs/
    ├── hasil/           # grafik training, confusion matrix, contoh prediksi
    ├── flowchart.md
    ├── laporan_ringkas.md
    └── Poster_UAS_KelompokXXX.pptx
```

## 10. Checklist Kelengkapan (sesuai Soal UAS Resmi)
- [ ] Program Python (folder `notebooks/`, `backend/`, `gui_web/`)
- [ ] Data asli (dari Kaggle, ditempatkan di `data/gojek_reviews.csv`)
- [ ] Laporan (dokumen ini + lampiran gambar dari `docs/hasil/`)
- [ ] Poster A3 dengan nama **"Poster UAS_KelompokXXX"** (`docs/Poster_UAS_KelompokXXX.pptx`)
- [ ] Link GitHub repo kelompok dicantumkan di laporan & poster
- [ ] File dikumpulkan dikompres dengan nama **"UAS_KelompokXXX.zip"**
- [ ] Dikumpulkan sebelum pukul 23.59 WIB di Hebat E-Learning

> Ganti semua "XXX" di atas dengan nomor kelompok kalian yang sebenarnya.
