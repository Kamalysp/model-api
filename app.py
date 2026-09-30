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

    if "kural 1" in question or "thirukkural 1" in question:
        return {
            "answer": "Thirukkural 1:\nஅகர முதல எழுத்தெல்லாம் ஆதி\nபகவன் முதற்றே உலகு\n\nMeaning: Just as A is the first of all letters, God is the first cause of the world."
        }
    if "kural 2" in question or "thirukkural 2" in question:
        return {
            "answer": "Thirukkural 2:\nகற்றதனால் ஆய பயனென்கொல் வாலறிவன்\nநற்றாள் தொழாஅர் எனின்\n\nMeaning: What is the use of all one's learning if they do not worship the feet of the one who possesses perfect knowledge?"
        }
    if "kural 3" in question or "thirukkural 3" in question:
        return {
            "answer": "Thirukkural 3:\nமலர்மிசை ஏகினான் மாணடி சேர்ந்தார்\nநிலமிசை நீடுவாழ் வார்\n\nMeaning: Those who reach the feet of Him who occupies the flower-like heart will live long upon this earth."
        }
    if "kural 4" in question or "thirukkural 4" in question:
        return {
            "answer": "Thirukkural 4:\nவேண்டுதல் வேண்டாமை இலானடி சேர்ந்தார்க்கு\nயாண்டும் இடும்பை இல\n\nMeaning: Those who have reached the feet of Him who is beyond desire and aversion will never suffer sorrow."
        }
    if "kural 5" in question or "thirukkural 5" in question:
        return {
            "answer": "Thirukkural 5:\nஇருள்சேர் இருவினையும் சேரா இறைவன்\nபொருள்சேர் புகழ்புரிந்தார் மாட்டு\n\nMeaning: The two kinds of deeds, good and evil, do not affect those who delight in the true praise of God."
        }
    if "kural 6" in question or "thirukkural 6" in question:
        return {
            "answer": "Thirukkural 6:\nபொறிவாயில் ஐந்தவித்தான் பொய்தீர் ஒழுக்க\nநெறிநின்றார் நீடுவாழ் வார்\n\nMeaning: Those who stand firmly in the faultless path of the One who has subdued the five senses will live long."
        }
    if "kural 7" in question or "thirukkural 7" in question:
        return {
            "answer": "Thirukkural 7:\nதனக்குவமை இல்லாதான் தாள்சேர்ந்தார்க் கல்லால்\nமனக்கவலை மாற்றல் அரிது\n\nMeaning: Except for those who have reached the feet of Him who is incomparable, it is difficult to remove the distress of the mind."
        }
    return {
   
        "answer": "Sorry, I don't know the answer yet!"
    }    

@app.get("/health")
def health():
    return {"status": "ok"}
