// AboutScreen: contoh tambahan Layout sederhana (Column, Container, Row)
// dan penggunaan named route (didaftarkan di main.dart - Materi 10: Navigasi).
import 'package:flutter/material.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Tentang Aplikasi"),
        backgroundColor: const Color(0xFF00AA13),
        foregroundColor: Colors.white,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text(
              "Gojek Sentiment Analysis App",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 12),
            Text(
              "Aplikasi ini dibuat sebagai bagian dari tugas mata kuliah "
              "Mobile Development, menerapkan konsep Flutter mulai dari "
              "widget, layout, navigasi, form dan validasi, state "
              "management, hingga integrasi REST API ke backend FastAPI "
              "yang menjalankan model machine learning (CNN-BiLSTM) untuk "
              "klasifikasi sentimen ulasan pengguna Gojek.",
            ),
            SizedBox(height: 20),
            Text(
              "Backend: FastAPI + TensorFlow\n"
              "Frontend: Flutter (Dart)\n"
              "Model terbaik: Model2_CNN_BiLSTM_Hybrid",
              style: TextStyle(color: Colors.grey),
            ),
          ],
        ),
      ),
    );
  }
}
