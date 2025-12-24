# Project Euler
# Distinct Primes Factors
# Problem 47
# https://projecteuler.net/problem=47
#
# """
# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 * 7
# 15 = 3 * 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2^2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.
# 
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
# """

import itertools

def prime_factors(n):
    factors = set()
    
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)

    if n > 1:
        factors.add(n)
    
    return factors

def distinct(sets):
    big = set()
    for set_ in sets:
        big = big | set_

    return len(set(big)) == len(big)

for a in range(1,1_000_000):
    factors_a = prime_factors(a)
    factors_b = prime_factors(a+1)
    factors_c = prime_factors(a+2)
    factors_d = prime_factors(a+3)

    if len(factors_a) == len(factors_b) == len(factors_c) == len(factors_d) == 4:
        if distinct([factors_a, factors_b, factors_c, factors_d]):
            print(a)
            break