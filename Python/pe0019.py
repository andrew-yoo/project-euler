# Project Euler
# Counting Sundays
# Problem 19
# https://projecteuler.net/problem=19
#
# """
# You are given the following information, but you may prefer to do some research for yourself.
# • 1 Jan 1900 was a Monday.
# • Thirty days has September, 
#   April, June and November. 
#   All the rest have thirty-one, 
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# • A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# """

import datetime as date

def count_first_of_month(start_year, end_year, start_month, end_month, weekday):
  result = 0
  for a in range(start_year, end_year + 1):
    for b in range(start_month, end_month + 1):
      if date.date(a, b, 1).weekday() == (weekday - 1):
        result += 1
  return result

count_first_of_month(1901, 2000, 1, 12, 7)
