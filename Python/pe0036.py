# Project Euler
# Double-base Palindromes
# Problem 36
# https://projecteuler.net/problem=36
#
# """
# The decimal number, 585 = 1001001001[2] (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# """

def base10_to_binary(number):
    binary = bin(number)[2:]
    return binary

double_base_palindromes = set()
  
for a in range(1_000_000):
    if list(str(a)) == list(reversed(str(a))) and list(str(base10_to_binary(a)))== list(reversed(str(base10_to_binary(a)))):
        double_base_palindromes.add(a)

print(sum(double_base_palindromes))
