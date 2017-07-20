#Euler - problem 7
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def isprime(num):
    i=3
    while i**2 <= num:
        if num%i == 0:
            return False
        else:
            i += 2
    return True


primecount = 6
num = 17
while primecount < 10001:
    if isprime(num):
        primecount += 1
    num = num + 2
else: print num - 2
