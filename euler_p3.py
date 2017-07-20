# Euler - problem 3
""" The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

from math import sqrt

N = 600851475143
maxval = int(sqrt(N))
factors = []
for i in range(3,maxval+1):
    if N % i == 0:
        factors.append(i)
        N /= i #IDEA: prime-factorization is unique, so divide by each factor to find remaining factors
        maxval = int(sqrt(N))

print factors
