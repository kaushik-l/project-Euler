#Euler - problem 4
""" A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the
product of two 3-digit numbers."""

Nmin = 100
Nmax = 999

# function to check if a number is factorizable as product of two three digit numbers
def factorize3digit(num):
    for i in range(999, 99, -1):
        if num%i == 0 and len(str(num/i)) == 3: return True
        else: continue
    return False

prodmin = Nmin**2
prodmax = Nmax**2
for num in range(prodmax, prodmin, -1): #IDEA: start from max and break out after success
    if str(num) == str(num)[::-1]: #IDEA: if palindrome, check if factors are three-digit numbers
        if factorize3digit(num):
            print num
            break
