# Laporan Proyek: Sentiment Analysis Ulasan Aplikasi Gojek

 1. Pendahuluan
Proyek ini merupakan pengembangan dari studi yang dilakukan pada jurnal
"Sentiment Analysis on Google Play Store Reviews to Measure User Perception
of the Gojek Application Using CNN" (JAIC, Polibatam), yang hanya menggunakan
1 model deep learning (CNN). Pada proyek ini ditambahkan model kedua, yaitu
**Hybrid CNN-BiLSTM**, sebagai pembanding untuk melihat apakah kombinasi
fitur lokal (CNN) dan konteks sekuensial (BiLSTM) mampu meningkatkan performa
klasifikasi sentimen.

 2. Dataset
- Sumber: Kaggle - "Gojek App Reviews Bahasa Indonesia" (ucupsedaya)
- Jenis: Data teks mentah (raw data), bukan gambar
- Label: Positif, Netral, Negatif (berdasarkan rating atau anotasi lexicon)
- Catatan: Repositori ini menyertakan dataset SAMPEL demo
  (`data/gojek_reviews_sample.csv`) karena proses eksekusi berada di lingkungan
  sandbox tanpa akses ke domain kaggle.com. Untuk hasil final, ganti dengan
  dataset asli sesuai instruksi pada `data/generate_sample_data.py`.

 3. Metodologi
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

 4. Hasil Training (Grafik Akurasi & Loss)
Grafik dihasilkan otomatis oleh `notebooks/train_and_evaluate.py` dan
tersimpan di `docs/hasil/`:
- `training_history_Model1_CNN.png`
- `training_history_Model2_CNN_BiLSTM_Hybrid.png`

*(Tempelkan gambar ini di laporan Word/PDF final sebagai lampiran "Hasil Training")*

 5. Hasil Testing (Confusion Matrix & Hasil Prediksi)
- Confusion matrix (gambar): `docs/hasil/confusion_matrix_Model1_CNN.png` dan
  `docs/hasil/confusion_matrix_Model2_CNN_BiLSTM_Hybrid.png`
- Contoh hasil prediksi pada data test: `docs/hasil/sample_predictions.csv`
  (berisi teks asli, label aktual, dan label hasil prediksi model terbaik)

 6. Tabel Perbandingan Model
Lihat file `models/comparison_results.csv` untuk hasil numerik lengkap hasil
run terakhir. Ringkasan (dari run demo dengan data sampel):

| Model                     | Accuracy | Precision | Recall | F1-score |
|---------------------------|----------|-----------|--------|----------|
| Model 1 - CNN              | 1.000    | 1.000     | 1.000  | 1.000    |
| Model 2 - Hybrid CNN-BiLSTM | 1.000    | 1.000     | 1.000  | 1.000    |

> Catatan: Akurasi 100% pada run demo terjadi karena dataset sampel bersifat
> sintetis dan sangat mudah dipisahkan antar kelas. Pada dataset Kaggle asli,
> hasil akan lebih bervariasi dan lebih merepresentasikan performa nyata
> kedua model. Jalankan ulang `notebooks/train_and_evaluate.py` setelah
> menempatkan `data/gojek_reviews.csv` (dataset asli) untuk mendapatkan
> hasil final yang valid untuk laporan.

 7. Link GitHub
Cantumkan link repository GitHub kelompok yang berisi seluruh source code
program Python final di sini: `https://github.com/<username>/<repo-kelompok>`

 8. Kesimpulan
- Pipeline end-to-end (preprocessing -> splitting -> training -> evaluasi ->
  pemilihan model -> deployment GUI) berhasil diimplementasikan dan diuji.
- Model terbaik dipilih secara otomatis oleh script berdasarkan F1-score
  dan langsung disimpan untuk digunakan oleh backend/GUI.
- Untuk laporan akhir yang dikumpulkan, wajib menjalankan ulang seluruh
  pipeline dengan dataset asli dari Kaggle agar angka evaluasi valid dan
  bisa dipertanggungjawabkan secara akademis.

 9. Struktur Proyek
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

 10. Checklist Kelengkapan (sesuai Soal UAS Resmi)
- [ ] Program Python (folder `notebooks/`, `backend/`, `gui_web/`)
- [ ] Data asli (dari Kaggle, ditempatkan di `data/gojek_reviews.csv`)
- [ ] Laporan (dokumen ini + lampiran gambar dari `docs/hasil/`)
- [ ] Poster A3 dengan nama **"Poster UAS_KelompokXXX"** (`docs/Poster_UAS_KelompokXXX.pptx`)
- [ ] Link GitHub repo kelompok dicantumkan di laporan & poster
- [ ] File dikumpulkan dikompres dengan nama **"UAS_KelompokXXX.zip"**
- [ ] Dikumpulkan sebelum pukul 23.59 WIB di Hebat E-Learning

> Ganti semua "XXX" di atas dengan nomor kelompok kalian yang sebenarnya.
