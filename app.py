from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load("model/model.pkl")

class InputData(BaseModel):
    question: str

@app.post("/predict")
def predict(data: InputData):
    

@app.get("/health")
def health():
    return {"status": "ok"}
