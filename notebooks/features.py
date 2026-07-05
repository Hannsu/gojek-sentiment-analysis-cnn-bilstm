"""
FEATURE EXTRACTION + IMBALANCE HANDLING
Token + padding untuk input Deep Learning, dan class_weight untuk imbalance.
"""
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight

MAX_WORDS = 5000
MAX_LEN = 40


def build_tokenizer(texts):
    tokenizer = Tokenizer(num_words=MAX_WORDS, oov_token="<OOV>")
    tokenizer.fit_on_texts(texts)
    return tokenizer


def texts_to_padded(tokenizer, texts):
    seqs = tokenizer.texts_to_sequences(texts)
    return pad_sequences(seqs, maxlen=MAX_LEN, padding="post", truncating="post")


def encode_labels(label_encoder: LabelEncoder, labels, fit=False):
    if fit:
        return label_encoder.fit_transform(labels)
    return label_encoder.transform(labels)


def get_class_weights(y_train_encoded):
    """Menangani IMBALANCE DATA lewat class weighting (tanpa perlu resampling)."""
    classes = np.unique(y_train_encoded)
    weights = compute_class_weight(class_weight="balanced", classes=classes, y=y_train_encoded)
    return dict(zip(classes, weights))
