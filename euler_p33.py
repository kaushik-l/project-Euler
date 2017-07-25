#Euler - problem 33
"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is
obtained by cancelling the 9s. We shall consider fractions like, 30/50 = 3/5, to be trivial
examples. There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator. If the product
of these four fractions is given in its lowest common terms, find the value of the denominator."""

from operator import mul

nums = []
dens = []
for num in range(1, 5):
    for den in range(num + 1, 9):
        for digit in range(1, 10):
            if float(str(num) + str(digit)) / float(str(digit) + str(den)) == float(num)/den:
                nums.append(int(str(num) + str(digit)))
                dens.append(int(str(digit) + str(den)))

print reduce(mul, nums) , reduce(mul, dens)
