// Model data hasil prediksi sentimen.
// Merepresentasikan response JSON dari endpoint /api/sentiment/predict
// pada backend FastAPI.
class SentimentResult {
  final String originalText;
  final String cleanText;
  final String predictedLabel;
  final double confidence;
  final Map<String, double> probabilities;

  SentimentResult({
    required this.originalText,
    required this.cleanText,
    required this.predictedLabel,
    required this.confidence,
    required this.probabilities,
  });

  // Factory constructor untuk parsing JSON dari API menjadi object Dart.
  factory SentimentResult.fromJson(Map<String, dynamic> json) {
    final rawProbs = Map<String, dynamic>.from(json['probabilities'] ?? {});
    return SentimentResult(
      originalText: json['original_text'] ?? '',
      cleanText: json['clean_text'] ?? '',
      predictedLabel: json['predicted_label'] ?? '',
      confidence: (json['confidence'] as num?)?.toDouble() ?? 0.0,
      probabilities: rawProbs.map(
        (key, value) => MapEntry(key, (value as num).toDouble()),
      ),
    );
  }
}

// Model data untuk satu baris riwayat prediksi.
// Merepresentasikan response JSON dari endpoint /api/sentiment/history
class HistoryItem {
  final int id;
  final String originalText;
  final String predictedLabel;
  final double confidence;
  final String createdAt;

  HistoryItem({
    required this.id,
    required this.originalText,
    required this.predictedLabel,
    required this.confidence,
    required this.createdAt,
  });

  factory HistoryItem.fromJson(Map<String, dynamic> json) {
    return HistoryItem(
      id: json['id'] ?? 0,
      originalText: json['original_text'] ?? '',
      predictedLabel: json['predicted_label'] ?? '',
      confidence: (json['confidence'] as num?)?.toDouble() ?? 0.0,
      createdAt: json['created_at'] ?? '',
    );
  }
}
