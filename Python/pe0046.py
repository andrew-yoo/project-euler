# Project Euler
# Goldbach's Other Conjecture
# Problem 46
# https://projecteuler.net/problem=46
#
# """
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# """

from sympy import isprime

def generate_primes(limit):
    primes = []
    for n in range(2, limit):
        if isprime(n):
            primes.append(n)
    return primes

def generate_squares(limit):
    squares = []
    for n in range(1,limit):
        squares.append(n*n)
    return squares
    
def generate_odd_composites(limit):
    odd_composites = []
    for n in range(9,limit,2):
        if not isprime(n):
            odd_composites.append(n)
    return odd_composites

def find_smallest():
    primes = generate_primes(5_000)
    squares = generate_squares(100)
    odd_composites = generate_odd_composites(10_000)
    for n in odd_composites:
        expressible = False
        for p in primes:
            for s in squares:
                if n == p + 2*s:
                    expressible = True
                    break
        if not expressible:
            return n
s
print(find_smallest())