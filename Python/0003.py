# Project Euler
# Largest Prime Factor
# Problem 3
# https://projecteuler.net/problem=3
#
# """
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
# """

import math
import secrets

# Modular inverse function
def modular_inverse(a, n):
  g = math.gcd(a, n)
  if g != 1:
    return None  # No modular inverse exists
  return pow(a, -1, n)

# Elliptic curve point addition
def elliptic_add(P, Q, a, n):
  if P == (0, 0):
    return Q
  if Q == (0, 0):
    return P
  if P[0] == Q[0] and P[1] != Q[1]:
    return (0, 0)  # Point at infinity

  if P == Q:
    numerator = (3 * P[0]**2 + a) % n
    denominator = (2 * P[1]) % n
  else:
    numerator = (Q[1] - P[1]) % n
    denominator = (Q[0] - P[0]) % n

  gcd = math.gcd(denominator, n)
  if gcd > 1:
    return gcd  # Factor

  denominator_inv = modular_inverse(denominator, n)
  if denominator_inv is None:
    return None  # No modular inverse

  lam = (numerator * denominator_inv) % n
  x_r = (lam**2 - P[0] - Q[0]) % n
  y_r = (lam * (P[0] - x_r) - P[1]) % n
  return (x_r, y_r)

# Lenstra ECM optimized for largest prime factor
def lenstra_ecm(n, max_curves=10000, max_iterations=10000): # Must be increased for larger/more complicated numbers to avoid false positives.
  for _ in range(max_curves):
    # Generates random curve parameters
    x = secrets.randbelow(n - 1) + 1
    y = secrets.randbelow(n - 1) + 1
    a = secrets.randbelow(n - 1) + 1
    b = (y**2 - x**3 - a * x) % n
    P = (x, y)

    # Validate curve (checks if discriminant is nonzero mod n)
    discriminant = (4 * a**3 + 27 * b**2) % n
    if math.gcd(discriminant, n) != 1:
      continue  # Invalid curve — try again

    try:
      Q = P
      for k in range(2, max_iterations):
        Q = elliptic_add(Q, P, a, n)
        if isinstance(Q, int):  # Factor found
          return Q
    except Exception:
      continue
  return None  # No factor found after max_curves

# Find largest factor
def largest_prime_factor(n):
  def is_prime(n):
# Check if is prime:
    if n < 2:
      return False
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False
    return True
  while True:
    factor = lenstra_ecm(n)
    if factor is None:
      break
    while n % factor == 0:
      n //= factor
    if n == 1 or is_prime(n):
      return max(factor, n)
  print(n)

largest_prime_factor(600851475143) # This is overly complicated because I mostly copied this from a code I already wrote for general prime factorization using the Lenstra ECM method
