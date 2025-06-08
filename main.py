from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("iris_model.pkl")  # Load trained model

# Request format
class IrisInput(BaseModel):
    features: list

@app.post("/predict")
def predict(data: IrisInput):
    prediction = model.predict(np.array(data.features).reshape(1, -1))
    return {"prediction": int(prediction[0])}
