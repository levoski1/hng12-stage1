from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import requests  # Missing import

from myfunction import (
    is_armstrong,
    is_even,
    is_perfect,
    is_prime,
)

# Initialize FastAPI
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


@app.get("/api/classify-number", status_code=200)
def get_api(number: str):  # Ensure number is an integer
    # Validate if number is an integer
    if not number.lstrip('-').isdigit():  # Allows negative numbers too
        return {
            "number": number,  # Keep the invalid input in response
            "error": True
        }

    number = int(number)  # Convert to integer after validation
    
    # Fetch fun fact from Numbers API
    fun_fact_url = f"http://numbersapi.com/{number}/math"
    try:
        fun_fact_response = requests.get(fun_fact_url)
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available"
    except:
        fun_fact = "Could not fetch fun fact"

    # Classify the number
    prime_status = is_prime(abs(number))
    perfect_status = is_perfect(abs(number))
    armstrong_status = is_armstrong(abs(number))

    properties = ["even" if is_even(abs(number)) else "odd"]
    if armstrong_status:
        properties.insert(0, "armstrong")

    digit_sum = sum(int(digit) for digit in str(abs(number)))
    # Return the classification result
    return {
        "number": str(number),
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }
