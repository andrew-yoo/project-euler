# Project Euler
# Permuted Multiples
# Problem 52
# https://projecteuler.net/problem=52
#
# """
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# """

t1 = time()


function list_digits(n::Integer)
    s = string(n)
    return [d for d in 0:9 if Char('0' + d) in s]
end


function answer()
    limit = 1_000_000

    for i in 1:limit

        digits = list_digits(i)
        
        if digits == list_digits(2i) == list_digits(3i) == list_digits(4i) == list_digits(5i) == list_digits(6i)
            return i
        end
    end

    return 0
end

println(answer())

t2 = time()
println(t2 - t1)