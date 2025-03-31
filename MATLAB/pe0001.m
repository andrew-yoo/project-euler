% Project Euler
% Multiples of 3 or 5
% Problem 1
% https://projecteuler.net/problem=1

% "
% If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
% Find the sum of all the multiples of 3 or 5 below 1000.
% " 

sum = 0;

for x = 1:999
    if(mod(x,3) == 0 || mod(x,5) == 0)
        sum = sum + x;
    end
end

sum
