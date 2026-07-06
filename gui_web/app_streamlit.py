"""
GUI WEB - Streamlit
Menggunakan model terbaik hasil evaluasi (Model1_CNN atau Model2_CNN_BiLSTM_Hybrid)
Cara jalankan:
    cd gui_web
    streamlit run app_streamlit.py
"""
import sys
import os
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.services.predict_service import predict_sentiment
from app.core.database import init_db, save_history, get_history

st.set_page_config(page_title="Gojek Review Sentiment Analysis", page_icon="🛵", layout="centered")
init_db()

st.title("🛵 Analisis Sentimen Ulasan Gojek")
st.caption("Model terbaik dipilih otomatis dari perbandingan CNN vs Hybrid CNN-BiLSTM")

with st.form("predict_form"):
    text_input = st.text_area("Masukkan teks ulasan Gojek:", height=120,
                               placeholder="Contoh: driver nya ramah banget dan cepat sampai...")
    submitted = st.form_submit_button("Analisis Sentimen")

if submitted:
    if not text_input.strip():
        st.warning("Teks ulasan tidak boleh kosong.")
    else:
        with st.spinner("Memproses..."):
            result = predict_sentiment(text_input)
            save_history(result["original_text"], result["predicted_label"], result["confidence"])

        label = result["predicted_label"]
        color = {"positif": "green", "negatif": "red", "netral": "orange"}.get(label, "blue")
        st.markdown(f"### Hasil: :{color}[{label.upper()}]")
        st.write(f"Confidence: **{result['confidence']*100:.2f}%**")
        st.write("Teks setelah preprocessing:", f"`{result['clean_text']}`")
        st.bar_chart(result["probabilities"])

st.divider()
st.subheader("📜 Riwayat Prediksi Terakhir")
history = get_history(10)
if history:
    st.table(history)
else:
    st.info("Belum ada riwayat prediksi.")
