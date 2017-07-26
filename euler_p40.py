# Euler - problem 40
"""An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000"""

from operator import mul

numlist = []
num = 0
numlist = ''
while len(numlist) < 1000000:
    num += 1
    numlist += str(num)

print reduce(mul, [int(numlist[10**i - 1]) for i in range(0, 7)])
