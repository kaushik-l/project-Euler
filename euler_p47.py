#Euler - problem 47
"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from math import sqrt

def isPrime(num):
    if num in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        return True
    elif num%2 == 0: return False
    elif num%3 == 0: return False
    else:
        i = 5
        k = 2
        while i**2 <= num:
            if num%i == 0: return False
            i += k
            k = 6 - k
        return True

def countdivisors(num):
    bignum = num
    primedivisors = {}
    i = 2
    while i <= int(sqrt(bignum)):
        if isPrime(i):
            while bignum % i == 0:
                if i not in primedivisors.keys(): primedivisors[i] = 0
                primedivisors[i] += 1
                bignum /= i
                if isPrime(bignum):
                    if bignum not in primedivisors.keys(): primedivisors[bignum] = 0
                    primedivisors[bignum] += 1
                    break
            if isPrime(bignum): break
            else:
                i += 1
        else: i += 1
    return len(primedivisors.keys())

num = 0
success = False
while not success:
    num += 1
    success = all([countdivisors(i)==4 for i in range(num, num+4)])

print(num)