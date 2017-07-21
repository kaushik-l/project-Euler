#Euler - problem 8
"""The four adjacent digits in the 1000-digit number in 1000digits.txt that have the greatest
product are 9 x 9 x 8 x 9 = 5832. Find the thirteen adjacent digits in the 1000-digit number that
have the greatest product. What is the value of this product?"""

# usage: python euler_p8.py digits.txt
import sys

def multiplydigits(digits):
    prod = 1
    for i in range(len(digits)): prod = prod*int(digits[i])
    return prod

f = open(sys.argv[1], 'rU')
digits = f.read()
digits = "".join(digits.split())
numdigits = len(digits)
numadjacent = 13
print max([multiplydigits(digits[i:i + numadjacent]) for i in range(0, numdigits - numadjacent)])
