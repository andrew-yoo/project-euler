# Project Euler
# Longest Collatz Sequence
# Problem 14
# https://projecteuler.net/problem=14
#
# """
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
# """

def collatz_length(number):
  length = 1 # Include the first number in the collatz length; doesn't really change the outcome, though
  while number != 1:
    if number % 2 == 0:
      number = number // 2
    elif number % 2 == 1:
      number = (3 * number) + 1
    length += 1
  return length

longest_chain = 0
longest_chain_seed = 0
for x in range(1000000,1,-1): # Running through the loop backwards speeds it up, because the longest chain in a given interval is *usually* near the high end
  if collatz_length(x) > longest_chain:
    longest_chain = collatz_length(x)
    longest_chain_seed = x

print(longest_chain_seed)
