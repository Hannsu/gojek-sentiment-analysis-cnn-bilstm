import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/sentiment_result.dart';

class ApiService {
  static const String baseUrl = "http://localhost:8000";

  // POST /api/sentiment/predict
  Future<SentimentResult> predictSentiment(String text) async {
    final url = Uri.parse("$baseUrl/api/sentiment/predict");

    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"text": text}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return SentimentResult.fromJson(data);
    } else {
      throw Exception(
        "Gagal memproses prediksi (status ${response.statusCode})",
      );
    }
  }

  // GET /api/sentiment/history
  Future<List<HistoryItem>> getHistory({int limit = 20}) async {
    final url = Uri.parse("$baseUrl/api/sentiment/history?limit=$limit");

    final response = await http.get(url);

    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((item) => HistoryItem.fromJson(item)).toList();
    } else {
      throw Exception(
        "Gagal mengambil riwayat (status ${response.statusCode})",
      );
    }
  }
}
