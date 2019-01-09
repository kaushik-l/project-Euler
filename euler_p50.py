# Euler - problem 50
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred. The longest sum of
consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

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

# generate list of primes up to 50000
primelist = []
for num in range(2,50001):
    if isPrime(num): primelist.append(num)

count, primesum = 21, 953
while primesum < 1100000:
    for indx in range(1, len(primelist)-count):
        if isPrime(sum(primelist[indx:indx+count])):
            primesum = sum(primelist[indx:indx + count])
            # print(primelist[indx:indx + count])
            print(str(count) + ':' + str(primesum))
            break
    count += 1
