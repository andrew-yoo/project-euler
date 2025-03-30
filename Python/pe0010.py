# Project Euler
# Summation of Primes
# Problem 10
# https://projecteuler.net/problem=10
#
# """
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# """

def sieve_of_eratosthenes(bound):
    # Create a boolean array of True values
    sieve = [True] * bound
    # 0 and 1 are not prime numbers
    sieve[0] = sieve[1] = False

    # Iterate through numbers and mark multiples as non-prime
    for x in range(2, int(bound ** 0.5) + 1):
        if sieve[x]:  # If the number is still marked as prime
            for y in range(x ** 2, bound, x):
                sieve[y] = False

    # Extract all numbers marked as prime
    primes = [z for z in range(bound) if sieve[z]]
    return primes

primes = sieve_of_eratosthenes(2000000)

print(sum(primes))
