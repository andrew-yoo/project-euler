# Project Euler
# Circular Primes
# Problem 35
# https://projecteuler.net/problem=35
#
# """
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?
# """

import itertools
import sympy

def rotate_list_left(input_list):
    return input_list[1:] + input_list[:1]

def generate_rotations(number):
    rotations = []
    digits = list(str(number))
    rotations.append(int(number))
    for a in range(len(digits) - 1):
        digits = rotate_list_left(digits)
        rotations.append(int(''.join(digits)))
    return rotations

def check_circular_prime(input_list):
    prime_counter = 0
    for b in input_list:
        if sympy.isprime(b):
            prime_counter += 1
    if prime_counter == len(input_list):
        return True
    else:
        return False

circular_primes = set()

for c in range(1_000_000):
    if check_circular_prime(generate_rotations(c)):
        circular_primes.add(c)

print(len(circular_primes))
