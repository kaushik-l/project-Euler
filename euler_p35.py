# Euler - problem 35
"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and
719, are themselves prime. There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97. How many circular primes are there below one million?"""

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

def circshift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def isCircPrime(num):
    seq = [digit for digit in str(num)]
    for n in range(1, len(seq) + 1):
        if not isPrime(int("".join(circshift(seq, n)))): return False
    return True

circularprimes = [2, 3, 5, 7, 11]
num = 13
k = 4
while num < 1000000:
    if isCircPrime(num): circularprimes.append(num)
    num += k
    k = 6 - k

print len(circularprimes)

"""Notes: A trick to speed up: for a given digit count, once we've checked all numbers with a
particular starting digit, we don't have to check any number containing that digit, because those
numbers have already been accounted for e.g. once we check 11-19, we don't have to check
any 2-digit number containing 1"""
