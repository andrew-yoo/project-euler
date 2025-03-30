# Project Euler
# Special Pythagorean Triplet
# Problem 9
# https://projecteuler.net/problem=9
#
# """
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
# """

import math
import numpy as np

def euclid_primitive_triples(limit):
    triples = []
    m = 2
    while len(triples) < limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:  # Check for coprimeness and one even
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                triples.append((a, b, c))
                if len(triples) >= limit:
                    break
        m += 1
    return triples

def find_triple_with_sum(triples, target_sum):
    for triple in triples: # Checks primitive triples
        if sum(triple) == target_sum:
            return triple

    # If no primitive triples work, checks non-primitive triples:
    for triple in triples:
        scale_factor = 2
        while sum(triple) * scale_factor <= target_sum:  # Scales the triple
            scaled_triple = tuple(x * scale_factor for x in triple)
            if sum(scaled_triple) == target_sum:
                return scaled_triple
            scale_factor += 1
    return None  # No triples were found; in practice, can raise number of generated primitive roots

solution = find_triple_with_sum(euclid_primitive_triples(100), 1000)

print(np.prod(solution))
