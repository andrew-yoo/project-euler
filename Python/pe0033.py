# Project Euler
# Digit Cancelling Fractions
# Problem 33
# https://projecteuler.net/problem=33
#
# """
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
# """

import math
import fractions

def check_curious(numerator, denominator):
  if (int(denominator[0]) == 0 or int(denominator[1]) == 0) or (numerator[0] != denominator[1] and numerator[1] != denominator[0]) or (int(numerator) / int(denominator) != int(numerator[0]) / int(denominator[1]) and int(numerator) / int(denominator) != int(numerator[1]) / int(denominator[0])):
    return(False)
  elif int(numerator) / int(denominator) == int(numerator[0]) / int(denominator[1]) and int(numerator) / int(denominator) < 1:
    return(True)
  elif int(numerator) / int(denominator) == int(numerator[1]) / int(denominator[0]) and int(numerator) / int(denominator) < 1:
    return(True)

curious = []

for x in range(10, 100):
    for y in range(10, 100):
        x_str = str(x).zfill(2)
        y_str = str(y).zfill(2)

        if check_curious(x_str, y_str) == True:
          curious.append([int(x_str),int(y_str)])

product = 1

for z in range(len(curious)):
  product *= fractions.Fraction(curious[z][0],curious[z][1])

print(product.denominator)
