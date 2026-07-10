// HomeScreen: contoh StatelessWidget + Layout (Scaffold, Column, Row,
// Container) + Navigasi (Materi 9 & 10).
import 'package:flutter/material.dart';
import 'predict_screen.dart';
import 'history_screen.dart';
import 'about_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Gojek Sentiment Analysis"),
        backgroundColor: const Color(0xFF00AA13),
        foregroundColor: Colors.white,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const SizedBox(height: 12),
            const Icon(Icons.motorcycle, size: 72, color: Color(0xFF00AA13)),
            const SizedBox(height: 12),
            const Text(
              "Analisis Sentimen Ulasan Gojek",
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            const Text(
              "Aplikasi mobile untuk memprediksi sentimen (positif / "
              "negatif / netral) dari ulasan pengguna menggunakan model "
              "CNN-BiLSTM Hybrid.",
              textAlign: TextAlign.center,
              style: TextStyle(color: Colors.grey),
            ),
            const SizedBox(height: 32),

            // Navigasi menggunakan Navigator.push (Materi 10: Navigasi & Routing)
            _MenuButton(
              icon: Icons.edit_note,
              label: "Prediksi Sentimen Baru",
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const PredictScreen()),
                );
              },
            ),
            const SizedBox(height: 12),
            _MenuButton(
              icon: Icons.history,
              label: "Riwayat Prediksi",
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const HistoryScreen()),
                );
              },
            ),
            const SizedBox(height: 12),
            _MenuButton(
              icon: Icons.info_outline,
              label: "Tentang Aplikasi",
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const AboutScreen()),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}

class _MenuButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onTap;

  const _MenuButton({
    required this.icon,
    required this.label,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 1,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: ListTile(
        leading: Icon(icon, color: const Color(0xFF00AA13)),
        title: Text(label),
        trailing: const Icon(Icons.chevron_right),
        onTap: onTap,
      ),
    );
  }
}
