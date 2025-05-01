# Project Euler
# Pandigital Prime
# Problem 41
# https://projecteuler.net/problem=41
#
# """
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?
# """

import sympy
from itertools import permutations

def find_largest_pandigital_prime():
    for n in range(9, 0, -1):
        digits = ''.join(str(i) for i in range(n, 0, -1))
        for perm in sorted(permutations(digits), reverse=True):
            num = int(''.join(perm))
            if sympy.isprime(num):
                # The first number should also be the largest
                return num

largest_prime = find_largest_pandigital_prime()
largest_prime
