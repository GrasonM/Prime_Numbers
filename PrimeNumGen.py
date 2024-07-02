import unittest

#Written and edited in Jupyter Notebook by Grason Moye

# returns true or false for prime numbers within provided range 
def is_prime(value: int) -> bool:
    #1 is neither prime nor composite
    if value <= 1:
        return False
    #2 is the smallest prime number and the only even prime number
    if value == 2:
        return True
    #Zero is neither prime nor composite
    if value % 2 == 0:
        return False
    #loops through the range of a provided number and checks for factors from 3 to the square root of the number
    for i in range(3, int(value**0.5) + 1, 2):
        #Zero is neither prime nor composite
        if value % i == 0:
            return False
    return True

# Prime number generator function - lists prime numbers between input integers
def prime_generator(start: int, end: int) -> list[int]:
    if start > end:
        #input correction if 1st number is greater than 2nd number
        start, end = end, start
    return [number for number in range(start, end + 1) if prime(number)]

# Command-line interface output
def main(start: int, end: int):
    primes = prime_generator(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

# Run the main function and input with a specific range (example: 1 {Enter Key}, 10 {Enter Key})
main(int(input("Input starting number: ")), int(input("Input ending number: ")))
