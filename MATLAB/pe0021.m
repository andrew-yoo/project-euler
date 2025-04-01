% Project Euler
% Amicable Numbers
% Problem 21
% https://projecteuler.net/problem=21

% "
% Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
% If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

% For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of  % 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

% Evaluate the sum of all the amicable numbers under 10000.
% "

x = 10000;
sum_div = zeros(1, x);

for n = 1:x
    divisors_n = divisors(n);
    sum_div(n) = sum(divisors_n) - n; % Exclude itself
end

amicable_numbers = [];

for a = 1:x
    b = sum_div(a);
    if b > a && b <= x && sum_div(b) == a % Exclude duplicates
        amicable_numbers = [amicable_numbers; a, b];
    end
end

disp(sum(sum(amicable_numbers)));
