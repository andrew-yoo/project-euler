# Project Euler
# 10 001st Prime
# Problem 7
# https://projecteuler.net/problem=7
#
# """
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# """

def sieve_of_eratosthenes(nth_prime):
    import math
    if nth_prime >= 6: # Standard upper bound for primes -- no reason to be fancy
      bound = int(nth_prime * (math.log(nth_prime) + math.log(math.log(nth_prime))))
    else: # Not necessary for the problem (because n>=6), but a rough upper bound for (1<n<6)
      bound = int((3/2) ** (nth_prime + 1))

    is_prime = [True] * (bound + 1)
    is_prime[0] = is_prime[1] = False  # Because 0, 1 are not primes

    for number in range(2, int(bound ** (1/2)) + 1):
        if is_prime[number]:
            for multiple in range(number ** 2, bound + 1, number):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes[nth_prime - 1]

sieve_of_eratosthenes(10001)
