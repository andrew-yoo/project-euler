# Project Euler
# Number Spiral Diagonals
# Problem 28
# https://projecteuler.net/problem=28
#
# """
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# """

import numpy as np

def generate_ulam_spiral(n):
  spiral = np.zeros((n, n), dtype=int)
  x = y = n // 2
  spiral[x][y] = 1
  num = 2 # Next number to be placed
  step = 1 # Magnitude of move

  while num <= n ** 2:
    for _ in range(step): # Right and down
      if num > n ** 2: 
        break
      y += 1
      spiral[x][y] = num
      num += 1
    for _ in range(step):
      if num > n ** 2: 
        break
      x += 1
      spiral[x][y] = num
      num += 1
    step += 1

    for _ in range(step): # Left and up
      if num > n ** 2: 
        break
      y -= 1
      spiral[x][y] = num
      num += 1
    for _ in range(step):
      if num > n ** 2: 
        break
      x -= 1
      spiral[x][y] = num
      num += 1
    step += 1

  return spiral

def sum_ulam_diagonals(n):
  spiral = generate_ulam_spiral(n)
  diagonal_sum = 0

  for z in range(n):
    diagonal_sum += spiral[z][z]  # NW - SE Diagonal
    diagonal_sum += spiral[z][n - z - 1]  # SW - NE Diagonal
  diagonal_sum -= 1
  return diagonal_sum

print(sum_ulam_diagonals(1001))
