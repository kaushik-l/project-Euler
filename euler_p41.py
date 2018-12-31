#Euler - problem 41
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime. What is the largest n-digit pandigital prime that exists?
 """

import itertools

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

def permute_digitsfromright(num, count):
    left, right = str(num)[:-count], str(num)[-count:]
    allpermutations = list(itertools.permutations((right)))
    novelpermutations = [''.join(item) for item in allpermutations if int(item[0]) != count]
    return [int(left + item) for item in novelpermutations]


for numdigits in range(9,0,-1):
    maxnum = [int(''.join(map(str, list(range(numdigits,0,-1)))))]
    numlist, count = maxnum[:], 1
    is_prime = False
    while not is_prime and count < numdigits+1:
        is_primelist = []
        for indx, num in enumerate(numlist):
            is_primelist.append(isPrime(num))
        primenumlist = [numlistval for is_primelistval, numlistval in zip(is_primelist, numlist) if is_primelistval]
        if primenumlist:
            is_prime = True
        else:
            count += 1
            numlist = permute_digitsfromright(maxnum[0], count)
    if is_prime: break

print(str(numdigits) + ' digits:', max(primenumlist))
