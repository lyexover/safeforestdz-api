
#main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .weather import get_weather_data
from .model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À ajuster en prod !
    allow_methods=["POST"],
)

@app.post("/predict")
async def predict_weather(city: str):
    weather_data = get_weather_data(city)
    prediction = predict(weather_data)
    return {**weather_data, "prediction": prediction}