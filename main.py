from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained ML model
model = joblib.load("pump_model.pkl")

app = FastAPI(title="Smart Irrigation AI Server")

# ================= DATA SCHEMA =================
class SensorData(BaseModel):
    temperature: float
    humidity: float
    soil_moisture: float
    water_level: float | None = None

# ================= API ENDPOINT =================
@app.post("/esp32/button")
def predict_pump(data: SensorData):
    features = np.array([[
        data.soil,
        data.temperature,
        data.humidity
    ]])

    prediction = int(model.predict(features)[0])

    return {
        "pump": prediction
    }

# ================= ROOT =================
@app.get("/")
def root():
    return {"status": "Smart Irrigation AI Running"}
