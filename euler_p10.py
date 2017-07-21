#Euler - problem 10
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

def isprime(num):
    i=2
    while i**2 <= num: #IDEA: this automatically yields 2 and 3 as prime
        if num%i == 0:
            return False
        elif i<5: i += 1
        else: i += 2
    return True

print sum([num for num in range(2, 2000000) if isprime(num)])
