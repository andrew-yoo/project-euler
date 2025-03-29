# Project Euler
# Largest Palindrome Product
# Problem 4
# https://projecteuler.net/problem=4
#
# """
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# """

def check_palindrome(num):
  num = str(num)
  first_half = ""
  second_half = ""
  palindromes = []

  if len(num) % 2 == 1:
    num = num[:len(num)//2] + num[len(num)//2 +1:] # If length is odd, remove middle value

  first_half = num[:len(num)//2 + len(num)%2]
  second_half = num[len(num)//2 + len(num)%2:]
  return(first_half == second_half[::-1]) # Returns a boolean

for x in range(100, 1000): # Generate numbers
  for y in range(100, 1000):
    if check_palindrome(x * y) == True:
      palindromes.append(x * y)

print(max(palindromes))
