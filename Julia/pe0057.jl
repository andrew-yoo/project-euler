# Project Euler
# Square Root Convergents
# Problem 57
# https://projecteuler.net/problem=57
#
# """
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# 
# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# 
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of 
# digits in the numerator exceeds the number of digits in the denominator.
# 
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
# """

t1 = time()

# It is easy enough to show that the denominators for the rational approximations are given by the Pell numbers: 1,2,5,12,29,70,169,408,....
# Similarly, the numerators are given by the Pell-Lucas Numbers: 3,7,17,41,99,239,577,....

function digit_count(n::Integer)
    counter = 0
    while n > 0
        n ÷= 10
        counter += 1
    end
    return counter
end

function generate_pell(limit::Integer)
    pells = BigInt[2, 5]
    for i in 3:limit
        next_term = BigInt(2) * pells[i-1] + pells[i-2]
        push!(pells, next_term)
    end
    return pells[1:limit]
end

function generate_pell_lucas(limit::Integer)
    pell_lucass = BigInt[3, 7]
    for i in 3:limit
        next_term = BigInt(2) * pell_lucass[i-1] + pell_lucass[i-2]
        push!(pell_lucass, next_term)
    end
    return pell_lucass[1:limit]
end

function answer()
    counter = 0
    denoms = generate_pell(1000)
    nums = generate_pell_lucas(1000)

    for i in 1:1000
        if digit_count(nums[i]) > digit_count(denoms[i])
            counter += 1
        end
    end
    return counter
end


println(answer())

t2 = time()
println(t2 - t1)