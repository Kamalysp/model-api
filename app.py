from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("thirukkural.json", "r", encoding="utf-8") as f:
    data = json.load(f)

kurals = {
    str(item["Number"]): item
    for item in data["kural"]
}

class InputData(BaseModel):
    question: str

@app.post("/predict")
def predict(data: InputData):
    question = data.question.lower()

    for number in kurals:
        if f"kural {number}" in question or f"thirukkural {number}" in question:
            kural = kurals[number]

            return {
                "answer": (
                    f"Thirukkural {number}:\n"
                    f"{kural['Line1']}\n"
                    f"{kural['Line2']}\n\n"
                    f"Meaning: {kural['Translation']}"
                )
            }

    return {
        "answer": "Sorry, I don't know the answer yet!"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

   
