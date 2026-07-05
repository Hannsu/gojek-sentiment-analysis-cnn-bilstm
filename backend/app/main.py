from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sentiment_router
from app.core.database import init_db

app = FastAPI(
    title="Gojek Review Sentiment Analysis API",
    description="Backend prediksi sentimen ulasan aplikasi Gojek (Model terbaik: CNN vs Hybrid CNN-BiLSTM)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
app.include_router(sentiment_router.router)


@app.get("/")
def root():
    return {"message": "Gojek Sentiment Analysis API aktif. Buka /docs untuk dokumentasi."}
