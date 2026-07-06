"""
Script ini membuat data SAMPEL untuk keperluan demo pipeline end-to-end.

PENTING:
Sandbox eksekusi ini tidak punya akses ke domain kaggle.com, jadi dataset asli
"Gojek App Reviews Bahasa Indonesia" (ucupsedaya) tidak bisa diunduh otomatis di sini.

CARA PAKAI DATASET ASLI:
1. Download manual dari:
   https://www.kaggle.com/datasets/ucupsedaya/gojek-app-reviews-bahasa-indonesia
2. Simpan file CSV-nya sebagai: data/gojek_reviews.csv
   (pastikan ada kolom teks review, mis. 'content' atau 'review', dan kolom 'score'/'rating')
3. Jalankan ulang preprocessing.py -> otomatis akan pakai file asli jika ada,
   fallback ke sample data jika tidak ditemukan.
"""
import pandas as pd
import numpy as np
import os

np.random.seed(42)

positive_templates = [
    "aplikasi gojek sangat membantu dan cepat",
    "driver ramah dan tepat waktu, mantap",
    "fitur gopay memudahkan transaksi sehari hari",
    "puas dengan layanan gofood pengiriman cepat",
    "aplikasi bagus tidak pernah error",
    "terima kasih gojek sangat membantu mobilitas saya",
    "promo dan diskon nya banyak sangat menguntungkan",
    "pelayanan driver sopan dan profesional",
    "update terbaru semakin lancar dan responsif",
    "sangat recommended aplikasi ojek online terbaik",
]

negative_templates = [
    "aplikasi sering error dan force close",
    "driver membatalkan pesanan seenaknya sangat kecewa",
    "harga tiba tiba naik tanpa alasan jelas",
    "susah dapat driver padahal jam sibuk",
    "customer service lambat merespon keluhan",
    "aplikasi lemot dan sering nge-lag",
    "GPS tidak akurat driver nyasar terus",
    "pembayaran gopay sering gagal saat checkout",
    "tampilan aplikasi membingungkan setelah update",
    "sangat kecewa dengan pelayanan akhir akhir ini",
]

neutral_templates = [
    "aplikasi biasa saja tidak ada yang istimewa",
    "kadang lancar kadang error tergantung jaringan",
    "cukup membantu meski masih ada kekurangan",
    "fiturnya standar sama seperti aplikasi lain",
    "lumayan untuk dipakai sehari hari",
    "perlu banyak perbaikan tapi masih bisa dipakai",
    "biasa saja tidak buruk tidak juga bagus",
    "kadang puas kadang kecewa tergantung driver",
    "aplikasi oke tapi harga kadang mahal",
    "so so masih perlu banyak improvement",
]


def make_rows(templates, label, score_range, n):
    rows = []
    for _ in range(n):
        base = np.random.choice(templates)
        noise_words = ["sih", "banget", "nih", "deh", "ya", ""]
        text = base + " " + np.random.choice(noise_words)
        score = np.random.choice(score_range)
        rows.append({"content": text.strip(), "score": score, "label": label})
    return rows


if __name__ == "__main__":
    n_per_class = 400
    data = []
    data += make_rows(positive_templates, "positif", [4, 5], n_per_class)
    data += make_rows(negative_templates, "negatif", [1, 2], int(n_per_class * 0.6))  # sengaja imbalance
    data += make_rows(neutral_templates, "netral", [3], int(n_per_class * 0.8))

    df = pd.DataFrame(data).sample(frac=1, random_state=42).reset_index(drop=True)
    out_path = os.path.join(os.path.dirname(__file__), "gojek_reviews_sample.csv")
    df.to_csv(out_path, index=False)
    print(f"Sample data tersimpan di: {out_path}")
    print(df['label'].value_counts())
