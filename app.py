from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model/model.pkl")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}

@app.get("/health")
def health():
    return {"status": "ok"}