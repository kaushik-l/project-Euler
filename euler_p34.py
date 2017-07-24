#Euler - problem 34
"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

from math import factorial

#IDEA: The sum of the factorial of the digits of the largets k-digit number is k*9!
# This sum cannot exceed the number for k>=7 (trial and error check)

total = 0
num = 10
while num < 7*factorial(9):
    strnum = str(num)
    """
    zerosandones = len([pos for pos, char in enumerate(strnum) if char == '1' or char == '0'])
    if num % 2 != 0 and zerosandones % 2 == 0: continue
    """
    if sum([factorial(int(strnum[i])) for i in range(0, len(strnum))]) == num:
        print num,
        total += num
    num += 1

print
print total
