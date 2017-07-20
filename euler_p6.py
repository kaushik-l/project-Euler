#Euler - problem 6
""" The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the
square of the sum is 3025 - 385 = 2640. Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum."""

#IDEA: sum to n = n(n + 1)/2; sum to n^2 = n(n + 1)(2n + 1)/6

def sum2n(n):
    return n*(n + 1)/2

def sum2nsquared(n):
    return n*(n + 1)*(2*n + 1)/6

print sum2n(100)**2 - sum2nsquared(100)
