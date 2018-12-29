#Euler - problem 24
"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
 What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? """

from math import factorial as fact
from math import floor as floor
from math import ceil as ceil

N = 1e6
digitsleft = list(range(10))
count = 0
num = []

for digit in range(9,-1,-1):
    quotient = floor(N/fact(digit)) if floor(N/fact(digit)) < ceil(N/fact(digit)) else floor(N/fact(digit)) - 1
    count = count + (quotient * fact(digit))
    N = N - (quotient * fact(digit))
    num.append(digitsleft[quotient])
    del digitsleft[quotient]
    if count > 1e6: break

print(''.join(map(str, num)))
