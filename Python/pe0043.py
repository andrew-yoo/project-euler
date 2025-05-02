# Project Euler
# Sub-string Divisibility
# Problem 43
# https://projecteuler.net/problem=43
#
# """
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# 
# Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this way, we note the following:
# 
# d[2]d[3]d[4]=406 is divisible by 2
# d[3]d[4]d[5]=063 is divisible by 3
# d[4]d[5]d[6]=635 is divisible by 5
# d[5]d[6]d[7]=357 is divisible by 7
# d[6]d[7]d[8]=572 is divisible by 11
# d[7]d[8]d[9]=728 is divisible by 13
# d[8]d[9]d[10]=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.
# """

import itertools

def check_property(input_: str):
    if int(input_[1] + input_[2] + input_[3]) % 2 != 0:
        return False
    elif int(input_[2] + input_[3] + input_[4]) % 3 != 0:
        return False
    elif int(input_[3] + input_[4] + input_[5]) % 5 != 0:
        return False
    elif int(input_[4] + input_[5] + input_[6]) % 7 != 0:
        return False
    elif int(input_[5] + input_[6] + input_[7]) % 11 != 0:
        return False
    elif int(input_[6] + input_[7] + input_[8]) % 13 != 0:
        return False
    elif int(input_[7] + input_[8] + input_[9]) % 17 != 0:
        return False
    else:
        return True

pandigitals = set(itertools.permutations(range(10),10))
divisable_pandigitals = set()

for pandigital in pandigitals:
    if check_property(''.join(map(str, pandigital))):
        divisable_pandigitals.add(int(''.join(map(str, pandigital))))

print(sum(divisable_pandigitals))
