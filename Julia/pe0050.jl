# Project Euler
# Consecutive Prime Sum
# Problem 50
# https://projecteuler.net/problem=50
#
# """
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# """

t1 = time()

using Primes

function find(upper)
    primes_list = Primes.primes(upper)
    number_primes = length(primes_list)

    # There are 78,498 primes less than 1000

    for len in 550:-1:1
        for i in 1:(number_primes - len)
            sub = primes_list[i:len+i]

            sub_sum = sum(sub)

            if Primes.isprime(sub_sum) && sub_sum < upper
                return sub_sum
            end
        end
    end
    return nothing
end

function main()
    println(find(1_000_000))
end

main()

t2 = time()
println(t2 - t1)