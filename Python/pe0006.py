# Project Euler
# Sum Square Difference
# Problem 6
# https://projecteuler.net/problem=6
#
# """
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# """
import time
t1 = time.perf_counter()


def sum_square_diff(x):
  sum_squares = 0
  square_sum = 0
  for item in x:
    sum_squares += (item * item)
    square_sum += item # Temporarily assigning the sum instead of making a new variable
  square_sum = square_sum * square_sum
  return square_sum - sum_squares

print(sum_square_diff(list(range(1,101))))

t2 = time.perf_counter()
print(round(t2 - t1, 4))