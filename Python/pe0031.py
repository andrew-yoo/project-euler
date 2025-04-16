# Project Euler
# Coin Sums
# Problem 31
# https://projecteuler.net/problem=31
#
# """
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# 
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# 
# How many different ways can £2 be made using any number of coins?
# """

coins = [200, 100, 50, 20, 10, 5, 2, 1]
target = 200
solutions = []

current = [0 for x in range(8)]


remaining_after = target # You start with the full target value

for a in range(target // coins[0] + 1):
    current[0] = a
    remaining_after = target - a * coins[0]
    
    for b in range(remaining_after // coins[1] + 1):
        current[1] = b
        remaining_after = target - (a * coins[0] + b * coins[1])
        
        for c in range(remaining_after // coins[2] + 1):
            current[2] = c
            remaining_after = target - (a * coins[0] + b * coins[1] + c * coins[2])
            
            for d in range(remaining_after // coins[3] + 1):
                current[3] = d
                remaining_after = target - (a * coins[0] + b * coins[1] + c * coins[2] + d * coins[3])
                
                for e in range(remaining_after // coins[4] + 1):
                    current[4] = e
                    remaining_after = target - (a * coins[0] + b * coins[1] + c * coins[2] + d * coins[3] + e * coins[4])
                    
                    for f in range(remaining_after // coins[5] + 1):
                        current[5] = f
                        remaining_after = target - (a * coins[0] + b * coins[1] + c * coins[2] + d * coins[3] + e * coins[4] + f * coins[5])
                        
                        for g in range(remaining_after // coins[6] + 1):
                            current[6] = g
                            remaining_after = target - (a * coins[0] + b * coins[1] + c * coins[2] + d * coins[3] + e * coins[4] + f * coins[5] + g * coins[6])
                            
                            current[7] = remaining_after # Whatever is left
                            
                            if sum(current[y] * coins[y] for y in range(8)) == target: # Check if the total value equals the target
                                solutions.append(current)

print(len(solutions))
