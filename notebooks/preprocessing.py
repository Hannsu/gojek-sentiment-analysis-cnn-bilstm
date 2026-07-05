"""
PREPROCESSING PIPELINE
Input -> Cleaning -> Case Folding -> Tokenisasi -> Stopword Removal -> Stemming
Sesuai alur WAJIB: Input > Preprocessing > Data Splitting
"""
import os
import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
REAL_CSV = os.path.join(DATA_DIR, "gojek_reviews.csv")     
SAMPLE_CSV = os.path.join(DATA_DIR, "gojek_reviews_sample.csv")

stemmer = StemmerFactory().create_stemmer()
stopword_remover = StopWordRemoverFactory().create_stop_word_remover()


def clean_text(text: str) -> str:
    text = str(text).lower()                                  # case folding
    text = re.sub(r"http\S+|www\S+", " ", text)                # hapus URL
    text = re.sub(r"[^a-zA-Z\s]", " ", text)                   # hapus angka & simbol
    text = re.sub(r"\s+", " ", text).strip()                   # rapikan spasi
    return text


def preprocess_text(text: str) -> str:
    text = clean_text(text)
    text = stopword_remover.remove(text)                       # stopword removal
    text = stemmer.stem(text)                                  # stemming
    return text


def label_from_score(score: int) -> str:
    """Fallback labeling berbasis rating jika dataset tidak punya kolom label."""
    if score >= 4:
        return "positif"
    elif score == 3:
        return "netral"
    else:
        return "negatif"


def load_dataset() -> pd.DataFrame:
    if os.path.exists(REAL_CSV):
        print(f"[INFO] Memakai dataset ASLI: {REAL_CSV}")
        df = pd.read_csv(REAL_CSV)
        # sesuaikan nama kolom dataset Kaggle: umumnya 'content' & 'score'
        text_col = "content" if "content" in df.columns else df.columns[0]
        df = df.rename(columns={text_col: "content"})
        if "label" not in df.columns:
            score_col = "score" if "score" in df.columns else "rating"
            df["label"] = df[score_col].apply(label_from_score)
    else:
        print(f"[WARNING] Dataset asli tidak ditemukan di {REAL_CSV}.")
        print(f"[INFO] Memakai dataset SAMPLE (demo) sebagai gantinya: {SAMPLE_CSV}")
        df = pd.read_csv(SAMPLE_CSV)

    df = df.dropna(subset=["content"]).reset_index(drop=True)
    return df


def run_preprocessing(save_path=None):
    df = load_dataset()
    print("[INFO] Menjalankan cleaning + stopword removal + stemming...")
    df["clean_text"] = df["content"].apply(preprocess_text)
    df = df[df["clean_text"].str.len() > 0].reset_index(drop=True)

    if save_path is None:
        save_path = os.path.join(DATA_DIR, "processed.csv")
    df.to_csv(save_path, index=False)
    print(f"[INFO] Data hasil preprocessing disimpan di: {save_path}")
    print(df["label"].value_counts())
    return df


def split_data(df: pd.DataFrame, test_size=0.2, val_size=0.1, random_state=42):
    """Data Splitting: train / validation / test (stratified)."""
    train_df, temp_df = train_test_split(
        df, test_size=(test_size + val_size), stratify=df["label"], random_state=random_state
    )
    rel_val = val_size / (test_size + val_size)
    val_df, test_df = train_test_split(
        temp_df, test_size=(1 - rel_val), stratify=temp_df["label"], random_state=random_state
    )
    print(f"[INFO] Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")
    return train_df.reset_index(drop=True), val_df.reset_index(drop=True), test_df.reset_index(drop=True)


if __name__ == "__main__":
    df = run_preprocessing()
    train_df, val_df, test_df = split_data(df)
    train_df.to_csv(os.path.join(DATA_DIR, "train.csv"), index=False)
    val_df.to_csv(os.path.join(DATA_DIR, "val.csv"), index=False)
    test_df.to_csv(os.path.join(DATA_DIR, "test.csv"), index=False)
