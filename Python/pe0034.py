# Project Euler
# Digit Factorials
# Problem 34
# https://projecteuler.net/problem=34
#
# """
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# """

import math

def check_curious(num):
  num_digits = []
  for a in range(len(str(num))):
    num_digits.append(int(str(num)[a]))
  
  truth = 0
  for item in num_digits:
    truth += math.factorial(item)
  return(truth == num)

curious = set()

for x in range(10, 100000): # Can be adjusted
  if check_curious(x):
    curious.add(x)

print(sum(curious))
