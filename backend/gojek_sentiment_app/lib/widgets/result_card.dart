// Widget custom untuk menampilkan hasil prediksi.
// Contoh Layout gabungan Container, Column, Row, dan Padding
// (Materi 9: Layout Flutter).
import 'package:flutter/material.dart';
import '../models/sentiment_result.dart';

class ResultCard extends StatelessWidget {
  final SentimentResult result;

  const ResultCard({super.key, required this.result});

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
    final color = _colorForLabel(result.predictedLabel);

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: color.withOpacity(0.08),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: color.withOpacity(0.4)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                "Label: ${result.predictedLabel}",
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: color,
                ),
              ),
              Text(
                "${(result.confidence * 100).toStringAsFixed(1)}%",
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                  color: color,
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          const Text(
            "Teks asli:",
            style: TextStyle(fontWeight: FontWeight.w600, fontSize: 13),
          ),
          Text(result.originalText),
          const SizedBox(height: 8),
          const Text(
            "Probabilitas tiap kelas:",
            style: TextStyle(fontWeight: FontWeight.w600, fontSize: 13),
          ),
          ...result.probabilities.entries.map(
            (e) => Padding(
              padding: const EdgeInsets.only(top: 4),
              child: Row(
                children: [
                  SizedBox(width: 90, child: Text(e.key)),
                  Expanded(
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(6),
                      child: LinearProgressIndicator(
                        value: e.value,
                        minHeight: 8,
                        backgroundColor: Colors.grey.shade200,
                        color: _colorForLabel(e.key),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text("${(e.value * 100).toStringAsFixed(0)}%"),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
