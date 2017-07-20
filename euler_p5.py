#Euler - problem 5
""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder. What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?"""

# This code solves the more general problem of finding the smallest positive integer evenly
# divisible by all numbers from 1 to maxfactor

from operator import mul
from math import sqrt

def isfactor(num1, num2):
    return num1%num2 == 0

factors = [1]
maxfactor = 20
duplicates = []
for num in range(2, maxfactor + 1):
        #IDEA: add number to factor set only if it is not a factor of the product of existing factors
        if not isfactor(reduce(mul, factors), num):
            factors.append(num)
            #IDEA: remove factors of factors
            for factor in factors[:-1]:
                if isfactor(factors[-1], factor):
                    del factors[factors.index(factor)]
                    break

print reduce(mul, factors)
