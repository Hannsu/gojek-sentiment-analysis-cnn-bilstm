// Entry point aplikasi Flutter.
// Mendemonstrasikan:
// - Setup MaterialApp & tema (Layout dasar - Materi 9)
// - Named routes (Navigasi & Routing - Materi 10)
// - ChangeNotifierProvider untuk State Management global (Materi 12)
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'providers/sentiment_provider.dart';
import 'screens/home_screen.dart';
import 'screens/predict_screen.dart';
import 'screens/history_screen.dart';
import 'screens/about_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => SentimentProvider(),
      child: MaterialApp(
        title: 'Gojek Sentiment Analysis',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primaryColor: const Color(0xFF00AA13),
          colorScheme: ColorScheme.fromSeed(
            seedColor: const Color(0xFF00AA13),
          ),
          useMaterial3: true,
        ),
        // Named routes (alternatif dari Navigator.push langsung di HomeScreen)
        initialRoute: '/',
        routes: {
          '/': (context) => const HomeScreen(),
          '/predict': (context) => const PredictScreen(),
          '/history': (context) => const HistoryScreen(),
          '/about': (context) => const AboutScreen(),
        },
      ),
    );
  }
}
