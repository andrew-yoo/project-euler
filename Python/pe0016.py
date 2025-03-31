# Project Euler
# Power Digit Sum
# Problem 16
# https://projecteuler.net/problem=16
#
# """
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# """

def sum_of_digits(number):
  number = str(number)
  digits = []
  for x in range(len(number)):
    digits.append(int(number[x]))
  return(sum(digits))

sum_of_digits(2 ** 1000)
