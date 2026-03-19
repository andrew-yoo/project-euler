# Project Euler
# Power Digit Sum
# Problem 16
# https://projecteuler.net/problem=16
#
# """
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# """
import time

t1 = time.perf_counter()


def sum_of_digits(number):
    number = str(number)
    digits = []
    for x in range(len(number)):
        digits.append(int(number[x]))
    return sum(digits)


def answer():
    return sum_of_digits(2**1000)


print(answer())

t2 = time.perf_counter()
print(round(t2 - t1, 4))
