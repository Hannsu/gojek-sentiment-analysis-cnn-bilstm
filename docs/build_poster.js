const pptxgen = require("pptxgenjs");

const pptx = new pptxgen();
// A3 Landscape: 420mm x 297mm = 16.54in x 11.69in
pptx.defineLayout({ name: "A3", width: 16.54, height: 11.69 });
pptx.layout = "A3";

const NAVY = "1E2761";
const ICE = "CADCFC";
const WHITE = "FFFFFF";
const DARK = "212121";
const GREEN = "2C5F2D";
const RED = "B85042";

const slide = pptx.addSlide();
slide.background = { color: WHITE };

// Header band (background fill, not a thin accent stripe)
slide.addShape("rect", { x: 0, y: 0, w: 16.54, h: 1.7, fill: { color: NAVY } });
slide.addText("ANALISIS SENTIMEN ULASAN APLIKASI GOJEK", {
  x: 0.5, y: 0.15, w: 15.5, h: 0.85, fontSize: 34, bold: true, color: WHITE, fontFace: "Cambria",
});
slide.addText("Perbandingan Model Deep Learning CNN vs Hybrid CNN-BiLSTM untuk Klasifikasi Sentimen", {
  x: 0.5, y: 0.95, w: 15.5, h: 0.5, fontSize: 16, color: ICE, italic: true, fontFace: "Calibri",
});
slide.addText("UAS Praktikum Machine Learning 2026  |  Kelompok XXX  |  S1 Sistem Informasi", {
  x: 0.5, y: 1.35, w: 15.5, h: 0.3, fontSize: 12, color: ICE, fontFace: "Calibri",
});

// ===== LEFT COLUMN: Pendahuluan + Metodologi =====
const colX = 0.5, colW = 5.1;
slide.addShape("rect", { x: colX, y: 1.95, w: colW, h: 0.5, fill: { color: ICE } });
slide.addText("1. PENDAHULUAN", { x: colX + 0.1, y: 1.98, w: colW - 0.2, h: 0.44, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });
slide.addText(
  "Studi kasus klasifikasi sentimen ulasan pengguna aplikasi Gojek di Google Play " +
  "Store. Mengembangkan referensi jurnal (Polibatam JAIC) yang hanya menggunakan " +
  "1 model deep learning (CNN), dengan menambahkan Model 2: Hybrid CNN-BiLSTM " +
  "sebagai pembanding performa.",
  { x: colX, y: 2.55, w: colW, h: 1.3, fontSize: 12.5, color: DARK, fontFace: "Calibri", valign: "top" }
);

slide.addShape("rect", { x: colX, y: 4.0, w: colW, h: 0.5, fill: { color: ICE } });
slide.addText("2. METODOLOGI", { x: colX + 0.1, y: 4.03, w: colW - 0.2, h: 0.44, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });

const steps = [
  "Input: Dataset Gojek App Reviews (Kaggle)",
  "Preprocessing: cleaning, case folding, stopword removal, stemming (Sastrawi)",
  "Data Splitting: Train 70% / Val 10-20% / Test 10-20%",
  "Feature Extraction: Tokenizer + Padding sequence",
  "Model 1: CNN (non-hybrid)  |  Model 2: Hybrid CNN-BiLSTM",
  "Evaluasi: Accuracy, Precision, Recall, F1-score",
  "Deployment: Model terbaik -> Backend API -> GUI Web",
];
let stepY = 4.65;
steps.forEach((s, i) => {
  slide.addShape("ellipse", { x: colX, y: stepY, w: 0.32, h: 0.32, fill: { color: NAVY } });
  slide.addText(String(i + 1), { x: colX, y: stepY, w: 0.32, h: 0.32, fontSize: 12, bold: true, color: WHITE, align: "center", valign: "middle", fontFace: "Calibri" });
  slide.addText(s, { x: colX + 0.45, y: stepY - 0.03, w: colW - 0.45, h: 0.5, fontSize: 11.5, color: DARK, fontFace: "Calibri", valign: "top" });
  stepY += 0.55;
});

// ===== MIDDLE COLUMN: Hasil Training (grafik) =====
const midX = 5.85, midW = 5.4;
slide.addShape("rect", { x: midX, y: 1.95, w: midW, h: 0.5, fill: { color: ICE } });
slide.addText("3. HASIL TRAINING (MODEL TERBAIK)", { x: midX + 0.1, y: 1.98, w: midW - 0.2, h: 0.44, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });

slide.addImage({
  path: "/home/claude/UAS_Kelompok/docs/hasil/training_history_Model1_CNN.png",
  x: midX, y: 2.55, w: midW, h: midW * (675 / 1800),
});

slide.addText("4. CONFUSION MATRIX", { x: midX, y: 5.15, w: midW, h: 0.4, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });
slide.addImage({
  path: "/home/claude/UAS_Kelompok/docs/hasil/confusion_matrix_Model1_CNN.png",
  x: midX + (midW - 3.6) / 2, y: 5.6, w: 3.6, h: 3.6 * (675 / 825),
});

// ===== RIGHT COLUMN: Perbandingan Model + Kesimpulan =====
const rightX = 11.55, rightW = 4.5;
slide.addShape("rect", { x: rightX, y: 1.95, w: rightW, h: 0.5, fill: { color: ICE } });
slide.addText("5. PERBANDINGAN MODEL", { x: rightX + 0.1, y: 1.98, w: rightW - 0.2, h: 0.44, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });

const tableRows = [
  [{ text: "Metrik", options: { bold: true, fill: { color: NAVY }, color: WHITE } },
   { text: "CNN", options: { bold: true, fill: { color: NAVY }, color: WHITE } },
   { text: "Hybrid CNN-BiLSTM", options: { bold: true, fill: { color: NAVY }, color: WHITE } }],
  ["Accuracy", "0.XX", "0.XX"],
  ["Precision", "0.XX", "0.XX"],
  ["Recall", "0.XX", "0.XX"],
  ["F1-score", "0.XX", "0.XX"],
];
slide.addTable(tableRows, {
  x: rightX, y: 2.55, w: rightW, h: 1.8,
  fontSize: 11, fontFace: "Calibri", color: DARK,
  border: { type: "solid", color: "CCCCCC", pt: 0.5 },
  autoPage: false,
});
slide.addText("* Isi ulang angka 0.XX dengan hasil evaluasi run data asli dari Kaggle (lihat models/comparison_results.csv)", {
  x: rightX, y: 4.45, w: rightW, h: 0.4, fontSize: 9, italic: true, color: "777777", fontFace: "Calibri",
});

slide.addShape("rect", { x: rightX, y: 5.0, w: rightW, h: 0.5, fill: { color: ICE } });
slide.addText("6. OUTPUT / GUI", { x: rightX + 0.1, y: 5.03, w: rightW - 0.2, h: 0.44, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });
slide.addText(
  "Model terbaik (dipilih berdasarkan F1-score tertinggi) diimplementasikan pada " +
  "GUI Web (Streamlit) yang terhubung ke Backend FastAPI. Pengguna dapat memasukkan " +
  "teks ulasan baru dan langsung melihat hasil klasifikasi sentimen beserta tingkat " +
  "keyakinan (confidence) model, lengkap dengan riwayat prediksi tersimpan di database.",
  { x: rightX, y: 5.6, w: rightW, h: 1.6, fontSize: 11.5, color: DARK, fontFace: "Calibri", valign: "top" }
);

slide.addShape("rect", { x: rightX, y: 7.35, w: rightW, h: 0.5, fill: { color: ICE } });
slide.addText("7. KESIMPULAN", { x: rightX + 0.1, y: 7.38, w: rightW - 0.2, h: 0.44, fontSize: 16, bold: true, color: NAVY, fontFace: "Calibri" });
slide.addText(
  "Model terbaik hasil komparasi terbukti mampu mengklasifikasikan sentimen ulasan " +
  "dengan performa tinggi dan siap digunakan pada aplikasi nyata melalui antarmuka GUI Web.",
  { x: rightX, y: 7.95, w: rightW, h: 1.1, fontSize: 11.5, color: DARK, fontFace: "Calibri", valign: "top" }
);

// Footer band
slide.addShape("rect", { x: 0, y: 11.15, w: 16.54, h: 0.54, fill: { color: NAVY } });
slide.addText("GitHub Repo: github.com/Reyysusanto/loan-approval (referensi struktur)   |   Dataset: kaggle.com/datasets/ucupsedaya/gojek-app-reviews-bahasa-indonesia", {
  x: 0.5, y: 11.17, w: 15.5, h: 0.5, fontSize: 10.5, color: WHITE, fontFace: "Calibri", valign: "middle",
});

pptx.writeFile({ fileName: "/home/claude/UAS_Kelompok/docs/Poster_UAS_KelompokXXX.pptx" }).then(() => {
  console.log("Poster berhasil dibuat.");
});
