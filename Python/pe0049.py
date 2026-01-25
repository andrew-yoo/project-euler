# Project Euler
# Prime Permutations
# Problem 49
# https://projecteuler.net/problem=49
#
# """
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this sequence?
# """"

from math import sqrt, ceil

def is_prime(n):
    for i in range(2,ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def primes_list(a, b):
    primes = []

    for i in range(1000, 10000):
        if is_prime(i):
            primes.append(i)
    
    return primes

def are_permutations(num1, num2):
    set1 = set(str(num1))
    set2 = set(str(num2))

    return (set1 == set2) and (len(set1) == len(set2))

def find():
    primes = primes_list(1_000, 10_000)
    for a in primes:
        for i in range(1, ceil((10_000 - a)/2)):
            b = a + i
            c = b + i

            if (b in primes) and (c in primes):
                if (are_permutations(a,b)) and (are_permutations(a,c)):
                    if a != 1487:
                        return a, b, c


def main():
    a, b, c = find()
    print(f'{a}{b}{c}')         

main()