from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import requests
from cachetools import cached, TTLCache
from myfunction import classify_number

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Create a cache with a TTL of 1 hour
cache = TTLCache(maxsize=1000, ttl=3600)

@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API"}

@cached(cache)
def get_fun_fact(num: int) -> str:
    fun_fact_url = f"http://numbersapi.com/{num}/math"
    try:
        fun_fact_response = requests.get(fun_fact_url, timeout=0.3)
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available"
    except requests.RequestException:
        fun_fact = "Could not fetch fun fact"
    return fun_fact

@app.get("/api/classify-number")
def get_api(number: str) -> Dict:
    try:
        num = int(number)
    except ValueError:
        return JSONResponse(status_code=400, content={"error": True, "number": number})
    fun_fact = get_fun_fact(num)
    result = classify_number(num)
    result["number"] = num
    result["fun_fact"] = fun_fact
    return result
