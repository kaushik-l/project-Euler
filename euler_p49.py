# Euler - problem 49
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there
is one other 4-digit increasing sequence.What 12-digit number do you form by concatenating the three terms
in this sequence?
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

def arithmetic_seq(list_of_vals):
    triplets = list(itertools.combinations(list_of_vals, 3))
    for triplet in triplets:
        if triplet[1] == (triplet[0] + triplet[2])/2: return triplet
    return []

# generate list of 4-digit primes
primedict = {}
for num in range(1001,9999):
    if isPrime(num):
        if ''.join(sorted(str(num))) not in primedict.keys():
            primedict[''.join(sorted(str(num)))] = [num]
        else:
            primedict[''.join(sorted(str(num)))].append(num)

# check 3 consecutive primes
count = 0
for key, val in primedict.items():
    if arithmetic_seq(val):
        print(arithmetic_seq(val))
        count += 1
        if count > 1: break
