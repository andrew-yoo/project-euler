# Project Euler
# Integer Right Triangles
# Problem 39
# https://projecteuler.net/problem=39
#
# """
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximised?
# """

def check_pythagorean_triple(tuple_):
    if tuple_[0]**2+ tuple_[1]**2 == tuple_[2]**2:
        return True
    else:
        return False

def generate_pythagorean_triples(perimeter):
    pythagorean_triples = set()
    perimeter = int(perimeter)
    for a in range(1, perimeter-2):
        for b in range(1, perimeter-a-1):
            c = perimeter - a - b
            if check_pythagorean_triple((a,b,c)):
                pythagorean_triples.add(c)
    return pythagorean_triples

perimeters = {}

for x in range(1001):
    perimeters[x] = len(generate_pythagorean_triples(x))

print(max(perimeters, key=perimeters.get))
