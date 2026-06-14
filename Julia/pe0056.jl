# Project Euler
# Powerful Digit Sum
# Problem 56
# https://projecteuler.net/problem=56
#
# """
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one
# followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
# """

t1 = time()

function digit_sum(n::Integer)
    result = 0
    while n > 0
        q = n ÷ 10
        result += Int(n % 10)
        n = q
    end
    return result
end

function answer()
    best = 0
    for a in 99:-1:1
        for b in 99:-1:1
            best = max(best, digit_sum(BigInt(a)^b))
        end
    end
    return best
end

println(answer())

t2 = time()
println(t2 - t1)