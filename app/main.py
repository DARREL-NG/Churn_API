import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

MODEL_PATH = "artifacts/XGBC_churn.pkl"

app = FastAPI(title="Churn Prediction API", version="1.1.0")

model = None

# 👉 Schéma d’entrée : TotalCharges peut être null
class CustomerInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: Optional[float] = None


@app.on_event("startup")
def load_model():
    global model
    model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.get("/schema")
def schema():
    # utile pour ton futur front-end
    return {
        "required_fields": [
            "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
            "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
            "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
            "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
            "MonthlyCharges"
        ],
        "optional_fields": ["TotalCharges"]
    }


@app.post("/predict")
def predict(payload: CustomerInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    data = payload.model_dump()

    # ✅ Gérer TotalCharges vide: on met NaN (comme dans ton notebook)
    if data.get("TotalCharges") is None:
        data["TotalCharges"] = float("nan")

    X = pd.DataFrame([data])

    # Proba churn = classe 1
    try:
        proba = float(model.predict_proba(X)[0][1])
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

    churn_label = "Yes" if proba >= 0.5 else "No"

    return {
        "churn": churn_label,
        "churn_probability": round(proba, 4),
        "threshold": 0.5
    }