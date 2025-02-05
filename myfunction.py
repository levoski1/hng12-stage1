from functools import lru_cache

@lru_cache(maxsize=1000)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True


@lru_cache(maxsize=1000)
def is_perfect(n):
    # Perfect numbers are positive
    if n <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n


@lru_cache(maxsize=1000)
def is_armstrong(n):
    # Handle negative numbers
    n = abs(n)
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == n


@lru_cache(maxsize=1000)
def digit_sum(n):
    # Use absolute value for digit sum
    return sum(int(digit) for digit in str(abs(n)))

def classify_number(number):
    # Absolute value for consistent processing
    abs_number = abs(number)
    
    properties = []
    
    if abs_number % 2 == 0:
        properties = ["armstrong", "even"] if is_armstrong(abs_number) else ["even"]
    else:
        properties = ["armstrong", "odd"] if is_armstrong(abs_number) else ["odd"]
    
    return {
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number)
    }