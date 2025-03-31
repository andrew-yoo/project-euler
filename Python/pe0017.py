# Project Euler
# Number Letter Counts
# Problem 17
# https://projecteuler.net/problem=17
#
# """
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# """

def letter_count(number):
  ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
  teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8} # Need to double-count 10 in both teens and tens
  tens = {10:3, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}
  hundreds = (7, 10) # "Hundred", "hundred and"

  if number < 10:
    return ones[number]
  elif number <20:
    return teens[number]
  elif number < 100:
    if number % 10 == 0:
      return tens[number]
    else:
      return tens[number - number % 10] + ones[number % 10]
  elif number < 1000:
    if number % 100 == 0:
      return ones[number // 100] + hundreds[0]
    else:
      return ones[number // 100] + hundreds[1] + letter_count(number % 100)
  elif number == 1000:
    return(11)

sum = 0
for x in range(1,1001):
  sum += letter_count(x)
print(sum)
