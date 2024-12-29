from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv
from redis_client import redis_client
from weather_service import WeatherService

load_dotenv()

app = FastAPI(title="Weather API Wrapper")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

weather_service = WeatherService()

@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "weather-api"}

@app.get("/weather/{city}")
async def get_weather(city: str):
    try:
        weather_data = await weather_service.get_weather(city)
        return weather_data
    except httpx.HTTPError as e:
        raise HTTPException("Internal Server Error")