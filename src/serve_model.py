# src/serve_model.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="🎯 Student Score Prediction API")


model = joblib.load("models/model.pkl")
columns = joblib.load("models/columns.pkl")


class StudentInput(BaseModel):
    study_time: float
    attendance: float
    gender: str  # "Male" or "Female"


@app.get("/")
def root():
    return {"message": "🚀 Student Score Predictor API is Live!"}


@app.post("/predict")
def predict_score(data: StudentInput):
    try:

        gender_Male = 1 if data.gender.lower() == "male" else 0

        input_dict = {
            "study_time": data.study_time,
            "attendance": data.attendance,
            "gender_Male": gender_Male,
        }

        for col in columns:
            if col not in input_dict:
                input_dict[col] = 0

        final_input = [input_dict[col] for col in columns]
        prediction = model.predict([final_input])[0]

        return {"predicted_score": round(prediction, 2)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
