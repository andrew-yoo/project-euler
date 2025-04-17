# Project Euler
# Pandigital Products
# Problem 32
# https://projecteuler.net/problem=32
#
# """
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# """

import itertools

def generate_digit_permutations(start, end):
    digits = ''.join(str(x) for x in range(start, end + 1))
    all_permutations = [''.join(y) for y in itertools.permutations(digits)]
    return all_permutations

pandigitals = set()

for p in generate_digit_permutations(1, 9):
    for a in range(1, 8):
        for b in range(a + 1, 9):
            x = int(p[:a])  # Multiplicand 
            y = int(p[a:b])  # Multiplier
            z = int(p[b:])  # Product
            
            if x * y == z:
                pandigitals.add(z) # Does nothing if product is a duplicate

print(sum(pandigitals)) 
