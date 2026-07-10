# Gojek Sentiment Analysis App (Flutter)

Aplikasi mobile Flutter untuk memprediksi sentimen ulasan Gojek, terhubung
ke backend FastAPI (model CNN-BiLSTM) yang sudah ada.

## Cara menjalankan

```bash
flutter pub get
flutter run
```

Sebelum menjalankan, sesuaikan alamat backend di
`lib/services/api_service.dart` (variabel `baseUrl`):
- Emulator Android → `http://10.0.2.2:8000`
- HP fisik satu jaringan WiFi → `http://<IP-lokal-komputer>:8000`
- Backend yang sudah dideploy (Railway/Heroku/dll) → URL production-nya

## Struktur project

```
lib/
├── main.dart                     # entry point, routing, provider setup
├── models/
│   └── sentiment_result.dart     # model data hasil prediksi & riwayat
├── screens/
│   ├── home_screen.dart          # menu utama + navigasi
│   ├── predict_screen.dart       # form input + validasi + hasil prediksi
│   ├── history_screen.dart       # daftar riwayat prediksi (ListView)
│   └── about_screen.dart         # halaman informasi
├── widgets/
│   ├── custom_button.dart        # StatelessWidget custom
│   └── result_card.dart          # tampilan hasil prediksi
├── services/
│   └── api_service.dart          # HTTP client ke backend FastAPI
└── providers/
    └── sentiment_provider.dart   # state management (ChangeNotifier)
```

## Pemetaan ke topik perkuliahan

| # | Topik Silabus | Diterapkan di |
|---|---|---|
| 2 | Sistem operasi mobile (Android & iOS) | Project di-build & diuji untuk kedua platform lewat `flutter run`; folder `android/` & `ios/` otomatis dibuat `flutter create` |
| 3 | Cross-platform & pengenalan Flutter | Seluruh project ini (satu codebase Dart untuk Android & iOS) |
| 4 | Arsitektur Flutter (Engine, Framework, Widget Tree) | `main.dart` (root widget `MyApp` → `MaterialApp` → widget tree turunannya) |
| 5 | Bahasa Dart – sintaks dasar & tipe data | Seluruh file `.dart`: variabel, `String`, `double`, `Map`, `List`, null-safety (`?`, `!`) |
| 6 | OOP pada Dart (class, object, inheritance, mixin) | `sentiment_result.dart` (class & factory constructor), semua `StatelessWidget`/`StatefulWidget` (inheritance dari class Flutter) |
| 8 | Widget (Stateless vs Stateful) | Stateless: `custom_button.dart`, `result_card.dart`, `home_screen.dart`, `about_screen.dart`. Stateful: `predict_screen.dart`, `history_screen.dart` |
| 9 | Layout (Row, Column, Container, Scaffold) | Semua screen menggunakan `Scaffold`, `Column`, `Row`, `Container`, `Padding`, `ListView.builder` |
| 10 | Navigasi & Routing | `main.dart` (named routes) + `home_screen.dart` (`Navigator.push`) |
| 11 | Form, Input, dan Validasi | `predict_screen.dart` (`Form`, `TextFormField`, `validator`, `GlobalKey<FormState>`) |
| 12 | State Management Dasar (setState) | `predict_screen.dart` & `history_screen.dart` pakai `StatefulWidget`; dikembangkan lebih lanjut dengan `Provider`/`ChangeNotifier` di `sentiment_provider.dart` |
| 13 | Akses Data (REST API) | `api_service.dart` (GET & POST ke endpoint FastAPI `/api/sentiment/predict` dan `/api/sentiment/history`) |

## Catatan untuk laporan

Backend (`repomix-output.xml` yang sebelumnya diunggah) sudah mencakup sisi
server: endpoint REST API, model ML, dan penyimpanan riwayat ke SQLite.
Project Flutter ini melengkapi sisi client, sehingga bersama-sama kedua
project ini mencakup seluruh topik silabus mata kuliah Mobile Development.
