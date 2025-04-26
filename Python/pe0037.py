# Project Euler
# Truncatable Primes
# Problem 37
# https://projecteuler.net/problem=37
#
# """
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
# """

import sympy

truncatable_primes = set()

def check_double_truncateable_prime(number_):
    str_number = str(number_)
    length = len(str_number)
    
    if number_ <= 7:
        return False

    if sympy.isprime(number_) == False:
        return False
    
    for a in range(0,length):
        if sympy.isprime(int(str_number[a:])) == False:
            return False

    for b in range(1,length+1):
        if sympy.isprime(int(str_number[:b])) == False:
            return False
    
    return True

def find_truncatable_primes():
    counter = 8
    while len(truncatable_primes) < 11:
          if check_double_truncateable_prime(counter):
              truncatable_primes.add(counter)
          counter += 1
    return (truncatable_primes)

print(sum(find_truncatable_primes()))
