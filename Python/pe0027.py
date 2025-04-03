
# Project Euler
# Quadratic Primes
# Problem 27
# https://projecteuler.net/problem=27
#
# """
# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4
# 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
# """

import sympy

longest_list = 0
product = 0

for a in range(-999,1000):
  for b in range(-1000,1001):
    prime_list = []
    n = 0
    while sympy.isprime(n ** 2 + a * n + b) == True:
      prime_list.append(n ** 2 + a * n + b)
      n += 1
    if len(prime_list) > longest_list:
      longest_list = len(prime_list)
      product = a * b

print(product)
