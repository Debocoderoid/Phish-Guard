from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

from feature_extractor import extract_features

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

    features = extract_features(url)

    input_df = pd.DataFrame([features])

    prediction = model.predict(input_df)[0]

    result = "phishing" if prediction == 1 else "legitimate"

    return {
        "url": url,
        "prediction": result
    }