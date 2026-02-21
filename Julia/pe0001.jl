# Project Euler
# Multiples of 3 or 5
# Problem 1
# https://projecteuler.net/problem=1
#
# """
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# """

t1 = time()

function main()
    counter = 0
    
    for i in 1:999
        if (i % 3 == 0) || (i % 5 == 0)
            counter += i
        end
    end
    
    return counter
end

println(main())

t2 = time()
println(t2 - t1)