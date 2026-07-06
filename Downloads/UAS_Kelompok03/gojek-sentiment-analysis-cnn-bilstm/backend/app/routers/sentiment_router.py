from fastapi import APIRouter, HTTPException
from app.models.schemas import ReviewRequest, PredictionResponse
from app.services.predict_service import predict_sentiment
from app.core.database import save_history, get_history

router = APIRouter(prefix="/api/sentiment", tags=["Sentiment"])


@router.post("/predict", response_model=PredictionResponse)
def predict(request: ReviewRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Teks review tidak boleh kosong")
    result = predict_sentiment(request.text)
    save_history(result["original_text"], result["predicted_label"], result["confidence"])
    return result


@router.get("/history")
def history(limit: int = 20):
    return get_history(limit)
