# Project Euler
# Lychrel Numbers
# Problem 55
# https://projecteuler.net/problem=55
#
# """
# If we take 47, reverse and add, 47 + 47 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,
# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
# That is, 349 took three iterations to arrive at a palindrome.
# 
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that
# never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of
# these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In
# addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty
# iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact,
# 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
# 4668731596684224866951378664 (53 iterations, 28-digits).
# 
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994,
# 
# How many Lychrel numbers are there below ten-thousand?
# 
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
# """

t1 = time()

function reverse(n::Integer)
    x = BigInt(abs(n))
    rev = BigInt(0)
    while x != 0
        rev = rev * 10 + (x % 10)
        x = div(x, 10)
    end
    return rev
end

function is_palindrome(n::Integer)
    if (n % 10 == 0) && (n ≠ 0)
        return false
    end
    return BigInt(n) == reverse(n)
end

function is_lychrel(n::Integer)
    n = BigInt(n)

    for i in 1:50
        n += reverse(n)

        if is_palindrome(n)
            return false
        end
    end
    return true
end

function answer()
    counter::Integer = 0
    limit::Integer = 9_999

    for n in 1:limit   # numbers below 10000
        if is_lychrel(n)
            counter += 1
        end
    end
    return counter
end

println(answer())

t2 = time()
println(t2 - t1)