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
    question = data.question.lower()

    if "thirukkural 1" in question or "kural 1" in question:
        return {
            "answer": "Thirukkural 1:\nஅகர முதல எழுத்தெல்லாம் ஆதி\nபகவன் முதற்றே உலகு\n\nMeaning: Just as 'A' is the first of all letters, God is the first cause of the world."
        }

    return {
        "answer": "Sorry, I don't know the answer yet!"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
