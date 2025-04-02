# Project Euler
# Reciprocal Cycles
# Problem 26
# https://projecteuler.net/problem=26
#
# """
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2  =  0.5
# 1/3  =  0.(3)
# 1/4  =  0.25
# 1/5  =  0.2
# 1/6  =  0.1(6)
# 1/7  =  0.(142857)
# 1/8  =  0.125
# 1/9  =  0.(1)
# 1/10 =  0.1
# 
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which ^1/[d] contains the longest recurring cycle in its decimal fraction part.

def cycle_length(input):
  if input == 0:
    return(0)
    
  remainders = {}
  digits = []
  current_value = 1
  position = 0

  while current_value != 0:
    current_value = (current_value % input)
    if current_value in remainders:
      cycle_start = remainders[current_value]
      cycle = digits[cycle_start:] # Verifies entire cycle
      return (len(cycle))
    remainders[current_value] = position
    digits.append(current_value * 10 // input)  # Adds produced digit
    current_value *= 10
    position += 1
  return(0)

greatest_seed = 0

for d in range(1000):
  if cycle_length(d) > greatest_seed:
    greatest_seed = d

print(greatest_seed)
