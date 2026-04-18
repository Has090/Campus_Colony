from fastapi import APIRouter
from app.schemas.ai import RentPredictionRequest
from app.services.ai_service import predict_rent

router = APIRouter(prefix="/ai", tags=["AI Model"])


@router.post("/predict-rent")
def predict_rent_api(request: RentPredictionRequest):

    data = request.dict()

    prediction = predict_rent(data)

    return {
        "success": True,
        "predicted_rent": round(prediction, 2)
    }