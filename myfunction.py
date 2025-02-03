def is_armstrong(num: int) -> bool:    
    """Check if a number is an Armstrong number."""
    if num < 1:
        return False
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

def is_even(num: int) -> bool:
    """check if a number is even number"""
    if num < 1:
        return False
    return True if num % 2 == 0 else False

def is_prime(num: int) -> bool:
    """check if a number is prime"""
    if num <= 1:
        return False
    for a in range(2, int(num ** 0.5) + 1):
        if num % a == 0:
            return False
    return True

def is_perfect(num: int) -> bool:
    """Check for a perfect number"""
    if num < 1:
        return False
    sum = 0
    for a in range(1, num):
        if num % a == 0:
            sum += a
    return sum == num
