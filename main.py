from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import httpx  # Faster async requests
import asyncio

from myfunction import (
    is_armstrong,
    is_even,
    is_perfect,
    is_prime,
)

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


async def fetch_fun_fact(number: int) -> str:
    """ Fetch fun fact asynchronously to avoid blocking response time. """
    fun_fact_url = f"http://numbersapi.com/{number}/math"
    try:
        async with httpx.AsyncClient(timeout=0.5) as client:
            response = await client.get(fun_fact_url)
            if response.status_code == 200:
                return response.text
    except httpx.RequestError:
        pass
    return "No fun fact available"


@app.get("/api/classify-number")
async def get_api(number: str):
    if not number.lstrip('-').isdigit():
        return {
            "number": number,
            "error": True
        }

    number = int(number)
    abs_number = abs(number)  # Avoid multiple calls to abs()

    # Run classification tasks in parallel using asyncio
    results = await asyncio.gather(
        asyncio.to_thread(is_prime, abs_number),
        asyncio.to_thread(is_perfect, abs_number),
        asyncio.to_thread(is_armstrong, abs_number),
        fetch_fun_fact(number)  # Asynchronous API request
    )

    prime_status, perfect_status, armstrong_status, fun_fact = results

    properties = ["even" if is_even(abs_number) else "odd"]
    if armstrong_status:
        properties.insert(0, "armstrong")

    digit_sum = sum(int(digit) for digit in str(abs_number))

    return {
        "number": number,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }
