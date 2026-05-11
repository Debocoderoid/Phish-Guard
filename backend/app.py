from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

from feature_extractor import extract_features

top_features = joblib.load("top_features.pkl")

app = FastAPI()

model = joblib.load("model.pkl")


class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "PhishGuard API running"}


@app.post("/predict")
def predict(data: URLRequest):

    url = data.url

    if len(url) < 5:
        raise HTTPException(status_code=400, detail="Invalid URL")

    features = extract_features(url)

    input_df = pd.DataFrame([features])

    input_df = input_df[top_features]

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]
    confidence = max(probability)

    result = "phishing" if prediction == 1 else "legitimate"

    return {"url": url, "prediction": result, "confidence": confidence * 100}
