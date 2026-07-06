from pydantic import BaseModel
from typing import Dict


class ReviewRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    original_text: str
    clean_text: str
    predicted_label: str
    confidence: float
    probabilities: Dict[str, float]
