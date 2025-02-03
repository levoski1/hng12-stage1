def is_armstrong(num: int) -> bool:
    """Check if a number is an Armstrong number."""
    if num < 1:
        return False
    digits = str(num)
    length = len(digits)
    return num == sum(int(digit) ** length for digit in digits)


def is_even(num: int) -> bool:
    """Check if a number is even."""
    return num % 2 == 0


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    # Check divisibility up to sqrt(num), skipping even numbers
    for a in range(5, int(num ** 0.5) + 1, 2):
        if num % a == 0:
            return False
    return True


def is_perfect(num: int) -> bool:
    """Check if a number is a perfect number."""
    if num < 2:
        return False

    total = 1  # Start with 1 (smallest divisor)
    for a in range(2, int(num ** 0.5) + 1):
        if num % a == 0:
            total += a
            if a != num // a:  # Avoid adding sqrt(n) twice if perfect square
                total += num // a

    return total == num
