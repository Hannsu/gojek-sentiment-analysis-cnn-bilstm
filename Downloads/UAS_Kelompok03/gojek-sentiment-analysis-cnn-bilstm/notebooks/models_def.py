"""
MODEL 1: CNN murni (replikasi pendekatan jurnal referensi - non-hybrid)
MODEL 2: Hybrid CNN-BiLSTM (nilai tambah 'sunnah': hybrid vs non-hybrid)
"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Embedding, Conv1D, MaxPooling1D, GlobalMaxPooling1D,
    Dense, Dropout, Bidirectional, LSTM
)
from tensorflow.keras.optimizers import Adam

VOCAB_SIZE = 5000
EMBED_DIM = 128
MAX_LEN = 40


def build_cnn_model(num_classes: int) -> Sequential:
    """MODEL 1 - CNN non-hybrid (sesuai jurnal referensi)."""
    model = Sequential([
        Embedding(input_dim=VOCAB_SIZE, output_dim=EMBED_DIM, input_length=MAX_LEN),
        Conv1D(filters=128, kernel_size=5, activation="relu"),
        MaxPooling1D(pool_size=2),
        Conv1D(filters=64, kernel_size=3, activation="relu"),
        GlobalMaxPooling1D(),
        Dense(64, activation="relu"),
        Dropout(0.4),
        Dense(num_classes, activation="softmax"),
    ], name="Model1_CNN")
    model.compile(optimizer=Adam(learning_rate=1e-3),
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model


def build_cnn_bilstm_model(num_classes: int) -> Sequential:
    """MODEL 2 - Hybrid CNN + BiLSTM (menangkap fitur lokal n-gram sekaligus konteks sekuensial)."""
    model = Sequential([
        Embedding(input_dim=VOCAB_SIZE, output_dim=EMBED_DIM, input_length=MAX_LEN),
        Conv1D(filters=128, kernel_size=5, activation="relu", padding="same"),
        MaxPooling1D(pool_size=2),
        Bidirectional(LSTM(64, return_sequences=False)),
        Dense(64, activation="relu"),
        Dropout(0.4),
        Dense(num_classes, activation="softmax"),
    ], name="Model2_CNN_BiLSTM_Hybrid")
    model.compile(optimizer=Adam(learning_rate=1e-3),
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model
