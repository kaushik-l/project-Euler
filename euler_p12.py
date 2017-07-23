#Euler - problem 12
"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th
triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... Let us list the factors of the first seven triangle numbers:
1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors. What is the value of the
first triangle number to have over five hundred divisors?"""

# This is a rather slow implementation, but will  produce the full prime factorization,
# not just the total number of factors

from math import sqrt
from operator import mul

def isprime(num):
    if num in [2, 3, 5, 7, 11, 13, 17, 19, 23]: return True
    if num % 2 == 0: return False
    i=3
    while i**2 <= num:
        if num % i == 0: return False
        else: i += 2
    return True

def mult(table):
    values = [value + 1 for value in table.values()]
    if len(values) == 0: return 0
    else: return reduce(mul, values)

def countdivisors(trianglenum):
    bignum = trianglenum
    primedivisors = {}
    i = 2
    while i <= int(sqrt(bignum)):
        if isprime(i):
            while bignum % i == 0:
                if i not in primedivisors.keys(): primedivisors[i] = 0
                primedivisors[i] += 1
                bignum /= i
                if isprime(bignum):
                    if bignum not in primedivisors.keys(): primedivisors[bignum] = 0
                    primedivisors[bignum] += 1
                    break
            if isprime(bignum): break
            else:
                i += 1
        else: i += 1
    return mult(primedivisors)


num = 9
numdivisors = 0
while numdivisors <= 6:
    num = num + 1
    trianglenum = num*(num + 1)/2
    numdivisors = countdivisors(trianglenum) #IDEA: use prime factorization to count divisors
print num, trianglenum, numdivisors

""""
Notes: number of divisors, d(n*(n+1)/2) =
d(n/2)*d(n+1) if n is evenly
d((n+1)/2)*d(n) if n is odd
"""
