# Euler - problem 23
"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is 1 through 5 pandigital. The product 7254 is
unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital. Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital. HINT: Some products can be obtained in more than
one way so be sure to only include it once in your sum."""

def check_unique_digits(n):
    digitList = []
    for digit in str(n):
        if digit not in digitList and digit != '0': digitList.append(digit)
    return len(str(n)) == len(digitList)

productList = []
numberList = [n for n in range(1, 1999) if check_unique_digits(n)]
for n1 in numberList:
    for n2 in numberList:
        strnum = str(n1) + str(n2) + str(n1*n2)
        if '0' not in strnum and len(strnum) == 9 and \
            check_unique_digits(strnum) and n1*n2 not in productList:
            productList.append(n1*n2)

print sum(productList)
