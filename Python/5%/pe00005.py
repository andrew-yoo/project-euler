# Project Euler
# Smallest Multiple
# Problem 5
# https://projecteuler.net/problem=5
#
# """
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# """

import math

# Technically I think math.lcm exists, but that kind of defeats the point
def lcm(x,y):
  return(abs(x * y) // math.gcd(x,y))

def lcm_list(list):
  temp = list[0]
  final = 0
  while final == 0:
    for item in list:
      temp = lcm(temp, item)
    final = temp
  print(final)

lcm_list([11,12,13,14,15,16,17,18,19,20]) # Ignoring redundant cases
