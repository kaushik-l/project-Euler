# Euler - problem 46
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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

# generate list of primes up to 1000
primelist = []
for num in range(2,10001):
    if isPrime(num): primelist.append(num)

# check conjecture for all odd numbers
for num in range(3,10001,2):
    thisprimelist = [i for i in primelist if i<=num]
    success = False
    for primenum in thisprimelist:
        if sqrt((num - primenum)/2) == int(sqrt((num - primenum)/2)):
            success = True
            break
    if not success:
        print('Goldbach conjecture not satisfied: ' + str(num))
        break