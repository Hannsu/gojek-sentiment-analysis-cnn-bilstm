import os
import json
import pickle
import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..")
MODEL_DIR = os.path.join(BASE_DIR, "models")
sys.path.append(os.path.join(BASE_DIR, "notebooks"))
from preprocessing import preprocess_text  # reuse fungsi cleaning+stopword+stemming

_model = None
_tokenizer = None
_label_encoder = None
_max_len = 40


def load_artifacts():
    global _model, _tokenizer, _label_encoder, _max_len
    if _model is None:
        _model = load_model(os.path.join(MODEL_DIR, "best_model.keras"))
        with open(os.path.join(MODEL_DIR, "tokenizer.pkl"), "rb") as f:
            _tokenizer = pickle.load(f)
        with open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "rb") as f:
            _label_encoder = pickle.load(f)
        with open(os.path.join(MODEL_DIR, "model_info.json")) as f:
            info = json.load(f)
            _max_len = info.get("max_len", 40)
    return _model, _tokenizer, _label_encoder


def predict_sentiment(text: str):
    model, tokenizer, le = load_artifacts()
    clean = preprocess_text(text)
    seq = tokenizer.texts_to_sequences([clean])
    padded = pad_sequences(seq, maxlen=_max_len, padding="post", truncating="post")
    probs = model.predict(padded, verbose=0)[0]
    pred_idx = int(np.argmax(probs))
    label = le.inverse_transform([pred_idx])[0]
    confidence = float(probs[pred_idx])
    return {
        "original_text": text,
        "clean_text": clean,
        "predicted_label": label,
        "confidence": round(confidence, 4),
        "probabilities": {cls: round(float(p), 4) for cls, p in zip(le.classes_, probs)},
    }
