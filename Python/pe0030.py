# Project Euler
# Digit Fifth Powers
# Problem 30
# https://projecteuler.net/problem=30
#
# """
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# """

def check_digit_power_sum(input_number,power):
    digit_powers = []
    input_string = str(input_number)
    for digit in range(len(input_string)):
        digit_powers.append(int(input_string[digit]) ** power)
    if sum(digit_powers) == input_number:
        return(True)
    else:
        return(False)

number_sum = 0
for x in range(2,200000): # Upper bound can be adjusted
    if check_digit_power_sum(x,5) == True:
        number_sum += x

print(number_sum)
