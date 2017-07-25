#Euler - problem 20
"""n! means n x (n - 1) x ... x 3 x 2 x 1
For example, 10! = 10x9x...2x1 = 3628800, and the sum of the digits in the
number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!"""

from operator import mul

print sum([int(char) for char in str(reduce(mul, [num for num in range(1, 101)]))])
