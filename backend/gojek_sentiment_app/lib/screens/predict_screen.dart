// PredictScreen: contoh StatefulWidget (Materi 8), Form & Validasi
// (Materi 11), serta konsumsi State Management via Provider (Materi 12)
// yang di baliknya memanggil REST API (Materi 13).
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/sentiment_provider.dart';
import '../widgets/custom_button.dart';
import '../widgets/result_card.dart';

class PredictScreen extends StatefulWidget {
  const PredictScreen({super.key});

  @override
  State<PredictScreen> createState() => _PredictScreenState();
}

class _PredictScreenState extends State<PredictScreen> {
  // GlobalKey untuk mengelola state Form (validasi).
  final _formKey = GlobalKey<FormState>();
  final _textController = TextEditingController();

  @override
  void dispose() {
    _textController.dispose();
    super.dispose();
  }

  // Fungsi validasi input Form.
  String? _validateText(String? value) {
    if (value == null || value.trim().isEmpty) {
      return "Teks ulasan tidak boleh kosong";
    }
    if (value.trim().length < 5) {
      return "Teks terlalu pendek (minimal 5 karakter)";
    }
    return null;
  }

  void _submit() {
    // Validasi form sebelum memanggil API.
    if (_formKey.currentState!.validate()) {
      final provider = context.read<SentimentProvider>();
      provider.predict(_textController.text.trim());
    }
  }

  @override
  Widget build(BuildContext context) {
    // Consumer akan otomatis rebuild saat SentimentProvider notifyListeners()
    // dipanggil (contoh State Management, Materi 12).
    return Scaffold(
      appBar: AppBar(
        title: const Text("Prediksi Sentimen"),
        backgroundColor: const Color(0xFF00AA13),
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Text(
                "Masukkan teks ulasan pengguna Gojek:",
                style: TextStyle(fontWeight: FontWeight.w600),
              ),
              const SizedBox(height: 8),
              TextFormField(
                controller: _textController,
                maxLines: 4,
                validator: _validateText,
                decoration: InputDecoration(
                  hintText: "Contoh: Aplikasinya bagus, driver ramah...",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),
              const SizedBox(height: 16),

              Consumer<SentimentProvider>(
                builder: (context, provider, _) {
                  return CustomButton(
                    label: "Prediksi Sekarang",
                    icon: Icons.send,
                    isLoading: provider.isLoading,
                    onPressed: _submit,
                  );
                },
              ),

              const SizedBox(height: 24),

              // Menampilkan hasil / error sesuai state dari provider.
              Consumer<SentimentProvider>(
                builder: (context, provider, _) {
                  if (provider.errorMessage != null) {
                    return Text(
                      "Error: ${provider.errorMessage}",
                      style: const TextStyle(color: Colors.red),
                    );
                  }
                  if (provider.lastResult != null) {
                    return ResultCard(result: provider.lastResult!);
                  }
                  return const SizedBox.shrink();
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
