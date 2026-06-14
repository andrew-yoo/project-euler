# Project Euler
# Combinatoric Selections
# Problem 53
# https://projecteuler.net/problem=53
#
# """
# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, C(5,3) = 10.
# In general, C(n,k) = n!/(r!(n-r)!), where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.
# It is not until n=23, that a value exceeds one-million: C(23,10) = 1144066.
# How many, not necessarily distinct, values of C(n,r) for 1 <= n <= 100, are greater than one-million?
# """

t1 = time()


# Julia has the built in `binomial` function for C(n,k).

function answer()
    counter::Int64 = 0
    for i in 23:100
        for j in 1:i
            if binomial(BigInt(i),BigInt(j)) > 1_000_000
                counter += 1
            end
        end
    end
    return counter
end

println(answer())

t2 = time()
println(t2 - t1)