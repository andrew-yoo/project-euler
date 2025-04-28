# Project Euler
# Pandigital Multiples
# Problem 38
# https://projecteuler.net/problem=38
#
# """
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# 
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
# """

def check_pandigital(input_):
    input_string = str(input_)
    return len(input_string) == 9 and set(input_string) == set("123456789")

def find_largest_pandigital():
    largest_pandigital = 0
    for x in range(1, 10_000):
        concatenated_product = ""
        n = 1
        while len(concatenated_product) < 9:
            concatenated_product += str(x * n)
            n += 1
        if check_pandigital(concatenated_product):
            largest_pandigital = max(largest_pandigital, int(concatenated_product))
    return largest_pandigital

find_largest_pandigital()
