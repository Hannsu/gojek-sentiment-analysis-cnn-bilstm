// HistoryScreen: contoh StatefulWidget yang memuat data (GET request)
// dari REST API melalui Provider saat initState (Materi 12 & 13),
// dan menampilkannya dengan ListView.builder (Layout - Materi 9).
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';
import '../providers/sentiment_provider.dart';

class HistoryScreen extends StatefulWidget {
  const HistoryScreen({super.key});

  @override
  State<HistoryScreen> createState() => _HistoryScreenState();
}

class _HistoryScreenState extends State<HistoryScreen> {
  @override
  void initState() {
    super.initState();
    // Ambil data riwayat begitu screen pertama kali dibuka.
    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<SentimentProvider>().loadHistory();
    });
  }

  String _formatDate(String iso) {
    try {
      final date = DateTime.parse(iso);
      return DateFormat('dd MMM yyyy, HH:mm').format(date);
    } catch (_) {
      return iso;
    }
  }

  Color _colorForLabel(String label) {
    switch (label.toLowerCase()) {
      case 'positif':
      case 'positive':
        return Colors.green;
      case 'negatif':
      case 'negative':
        return Colors.red;
      default:
        return Colors.orange;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Riwayat Prediksi"),
        backgroundColor: const Color(0xFF00AA13),
        foregroundColor: Colors.white,
      ),
      body: Consumer<SentimentProvider>(
        builder: (context, provider, _) {
          if (provider.isLoading) {
            return const Center(child: CircularProgressIndicator());
          }

          if (provider.errorMessage != null) {
            return Center(child: Text("Error: ${provider.errorMessage}"));
          }

          if (provider.history.isEmpty) {
            return const Center(child: Text("Belum ada riwayat prediksi."));
          }

          return RefreshIndicator(
            onRefresh: () => provider.loadHistory(),
            child: ListView.builder(
              padding: const EdgeInsets.all(12),
              itemCount: provider.history.length,
              itemBuilder: (context, index) {
                final item = provider.history[index];
                final color = _colorForLabel(item.predictedLabel);

                return Card(
                  margin: const EdgeInsets.symmetric(vertical: 6),
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: color.withOpacity(0.15),
                      child: Icon(Icons.chat_bubble_outline, color: color),
                    ),
                    title: Text(
                      item.originalText,
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                    ),
                    subtitle: Text(_formatDate(item.createdAt)),
                    trailing: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        Text(
                          item.predictedLabel,
                          style: TextStyle(
                            color: color,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        Text(
                          "${(item.confidence * 100).toStringAsFixed(0)}%",
                          style: const TextStyle(fontSize: 12),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          );
        },
      ),
    );
  }
}
