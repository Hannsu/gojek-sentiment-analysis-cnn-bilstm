// SentimentProvider adalah contoh State Management menggunakan package
// `provider` (Materi 12: State Management Dasar - dikembangkan dari konsep
// setState menuju state management yang bisa dibagi ke banyak widget/screen
// tanpa perlu passing data manual lewat constructor di setiap level).
import 'package:flutter/foundation.dart';
import '../models/sentiment_result.dart';
import '../services/api_service.dart';

class SentimentProvider extends ChangeNotifier {
  final ApiService _apiService = ApiService();

  SentimentResult? _lastResult;
  List<HistoryItem> _history = [];
  bool _isLoading = false;
  String? _errorMessage;

  SentimentResult? get lastResult => _lastResult;
  List<HistoryItem> get history => _history;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> predict(String text) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners(); // memberi tahu semua widget yang "listen" untuk rebuild

    try {
      final result = await _apiService.predictSentiment(text);
      _lastResult = result;
    } catch (e) {
      _errorMessage = e.toString();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> loadHistory() async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final items = await _apiService.getHistory();
      _history = items;
    } catch (e) {
      _errorMessage = e.toString();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  void clearResult() {
    _lastResult = null;
    notifyListeners();
  }
}
