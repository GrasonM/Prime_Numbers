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
    return [number for number in range(start, end + 1) if is_prime(number)]

# Command-line interface output
def main(start: int, end: int):
    primes = prime_generator(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

#Class that tests functions
class TestFunctions(unittest.TestCase):

    #tests prime boolean functionality
    def test_is_prime(self):
        self.assertFalse(is_prime(24))
        self.assertFalse(is_prime(72))
        self.assertTrue(is_prime(127))
        self.assertTrue(is_prime(137))
        self.assertFalse(is_prime(240))
        self.assertTrue(is_prime(277))
        self.assertFalse(is_prime(280))
        self.assertTrue(is_prime(293))

    #prime number generator output validity check
    def test_prime_generator(self):
        self.assertEqual(prime_generator(1, 10), [2, 3, 5, 7])
        self.assertEqual(prime_generator(10, 1), [2, 3, 5, 7])
        self.assertEqual(prime_generator(7900, 7920), [7901, 7907, 7919])

# Running the tests
unittest.main(argv=[''], verbosity=2, exit=False)

# Run the main function and input with a specific range (example: 1 {Enter Key}, 10 {Enter Key})
main(int(input("Input starting number: ")), int(input("Input ending number: ")))
