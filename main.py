from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from typing import Dict
import requests

from myfunction import classify_number  # Import the helper function

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API"}


@lru_cache(maxsize=1000)  # Cache results for efficiency
@app.get("/api/classify-number")
def get_api(number: str) -> Dict:
    try:
        # Convert the input to an integer
        num = int(number)
    except ValueError:
        return JSONResponse(status_code=400, content={"error": True, "number": number})

    # Fetch fun fact from Numbers API
    fun_fact_url = f"http://numbersapi.com/{num}/math"
    try:
        fun_fact_response = requests.get(fun_fact_url, timeout=0.3)  # Timeout to prevent delays
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available"
    except requests.RequestException:
        fun_fact = "Could not fetch fun fact"

    # Classify the number using the helper function
    result = classify_number(num)
    result["number"] = num  # Include the original number in the response
    result["fun_fact"] = fun_fact  # Add the fun fact

    return result
