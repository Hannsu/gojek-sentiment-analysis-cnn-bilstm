"""
TRAINING & EVALUASI
- Melatih Model 1 (CNN) dan Model 2 (Hybrid CNN-BiLSTM)
- Evaluasi: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Membandingkan & memilih model terbaik -> disimpan untuk GUI
"""
import os
import json
import pickle
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

from features import build_tokenizer, texts_to_padded, get_class_weights
from models_def import build_cnn_model, build_cnn_bilstm_model

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "hasil")
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)


def plot_training_history(history, model_name):
    """Grafik Model Accuracy & Model Loss ."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    axes[0].plot(history.history["accuracy"], label="Train Accuracy")
    axes[0].plot(history.history["val_accuracy"], label="Validation Accuracy")
    axes[0].set_title(f"Model Accuracy - {model_name}")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")
    axes[0].legend()

    axes[1].plot(history.history["loss"], label="Train Loss")
    axes[1].plot(history.history["val_loss"], label="Validation Loss")
    axes[1].set_title(f"Model Loss - {model_name}")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Loss")
    axes[1].legend()

    plt.tight_layout()
    out_path = os.path.join(DOCS_DIR, f"training_history_{model_name}.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"[INFO] Grafik training history disimpan: {out_path}")


def plot_confusion_matrix(y_true, y_pred, class_names, model_name):
    """Confusion matrix dalam bentuk gambar."""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5.5, 4.5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=class_names, yticklabels=class_names)
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Prediction")
    plt.ylabel("Actual")
    plt.tight_layout()
    out_path = os.path.join(DOCS_DIR, f"confusion_matrix_{model_name}.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"[INFO] Confusion matrix disimpan: {out_path}")


def evaluate(y_true, y_pred, model_name, class_names):
    metrics = {
        "model": model_name,
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average="macro", zero_division=0),
        "recall": recall_score(y_true, y_pred, average="macro", zero_division=0),
        "f1_score": f1_score(y_true, y_pred, average="macro", zero_division=0),
    }
    print(f"\n===== EVALUASI {model_name} =====")
    for k, v in metrics.items():
        if k != "model":
            print(f"{k:10s}: {v:.4f}")
    print(confusion_matrix(y_true, y_pred))
    print(classification_report(y_true, y_pred, zero_division=0))
    plot_confusion_matrix(y_true, y_pred, class_names, model_name)
    return metrics


def main():
    train_df = pd.read_csv(os.path.join(DATA_DIR, "train.csv"))
    val_df = pd.read_csv(os.path.join(DATA_DIR, "val.csv"))
    test_df = pd.read_csv(os.path.join(DATA_DIR, "test.csv"))

    for d in (train_df, val_df, test_df):
        d["clean_text"] = d["clean_text"].fillna("")

    # ---- Feature extraction ----
    tokenizer = build_tokenizer(train_df["clean_text"])
    X_train = texts_to_padded(tokenizer, train_df["clean_text"])
    X_val = texts_to_padded(tokenizer, val_df["clean_text"])
    X_test = texts_to_padded(tokenizer, test_df["clean_text"])

    le = LabelEncoder()
    y_train = le.fit_transform(train_df["label"])
    y_val = le.transform(val_df["label"])
    y_test = le.transform(test_df["label"])
    num_classes = len(le.classes_)

    class_weights = get_class_weights(y_train)  # handling imbalance
    print("[INFO] Class weights (imbalance handling):", dict(zip(le.classes_, class_weights.values())))

    results = []
    trained_models = {}

    class_names = list(le.classes_)

    # ---- MODEL 1: CNN ----
    print("\n[INFO] Training MODEL 1 (CNN)...")
    model1 = build_cnn_model(num_classes)
    hist1 = model1.fit(X_train, y_train, validation_data=(X_val, y_val),
                        epochs=15, batch_size=16, class_weight=class_weights, verbose=2)
    plot_training_history(hist1, "Model1_CNN")
    y_pred1 = np.argmax(model1.predict(X_test), axis=1)
    results.append(evaluate(y_test, y_pred1, "Model1_CNN", class_names))
    trained_models["Model1_CNN"] = model1

    # ---- MODEL 2: Hybrid CNN-BiLSTM ----
    print("\n[INFO] Training MODEL 2 (Hybrid CNN-BiLSTM)...")
    model2 = build_cnn_bilstm_model(num_classes)
    hist2 = model2.fit(X_train, y_train, validation_data=(X_val, y_val),
                        epochs=15, batch_size=16, class_weight=class_weights, verbose=2)
    plot_training_history(hist2, "Model2_CNN_BiLSTM_Hybrid")
    y_pred2 = np.argmax(model2.predict(X_test), axis=1)
    results.append(evaluate(y_test, y_pred2, "Model2_CNN_BiLSTM_Hybrid", class_names))
    trained_models["Model2_CNN_BiLSTM_Hybrid"] = model2

    # ---- Perbandingan & pemilihan model terbaik (berdasarkan F1-score) ----
    results_df = pd.DataFrame(results).sort_values("f1_score", ascending=False)
    print("\n===== TABEL PERBANDINGAN MODEL =====")
    print(results_df.to_string(index=False))

    best_row = results_df.iloc[0]
    best_name = best_row["model"]
    best_model = trained_models[best_name]
    print(f"\n[INFO] MODEL TERBAIK: {best_name} (F1-score={best_row['f1_score']:.4f})")

    # ---- Simpan artefak untuk GUI / backend ----
    best_model.save(os.path.join(MODEL_DIR, "best_model.keras"))
    with open(os.path.join(MODEL_DIR, "tokenizer.pkl"), "wb") as f:
        pickle.dump(tokenizer, f)
    with open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "wb") as f:
        pickle.dump(le, f)
    with open(os.path.join(MODEL_DIR, "model_info.json"), "w") as f:
        json.dump({"best_model": best_name, "max_len": 40}, f, indent=2)

    results_df.to_csv(os.path.join(MODEL_DIR, "comparison_results.csv"), index=False)
    print(f"\n[INFO] Model terbaik & artefak tersimpan di folder: {MODEL_DIR}")

    # ---- Simpan contoh hasil prediksi (lampiran wajib di laporan) ----
    sample_idx = np.random.choice(len(test_df), size=min(15, len(test_df)), replace=False)
    best_pred = y_pred1 if best_name == "Model1_CNN" else y_pred2
    sample_result = pd.DataFrame({
        "text": test_df.iloc[sample_idx]["content"].values,
        "actual_label": le.inverse_transform(y_test[sample_idx]),
        "predicted_label": le.inverse_transform(best_pred[sample_idx]),
    })
    sample_result.to_csv(os.path.join(DOCS_DIR, "sample_predictions.csv"), index=False)
    print(f"[INFO] Contoh hasil prediksi disimpan: {os.path.join(DOCS_DIR, 'sample_predictions.csv')}")


if __name__ == "__main__":
    main()
