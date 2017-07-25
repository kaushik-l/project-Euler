#Euler - problem 21
"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
evenly into n). If d(a) = b and d(b) = a, where a not equal to b, then a and b are an amicable pair
and each of a and b are called amicable numbers. For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220. Evaluate the sum of all the amicable numbers under 10000."""

def sumofdivisors(num):
    if num in [0, 1]: return 0
    divisors = [1]
    i = 2
    while i**2 <= num:
        if num % i == 0:
            divisors += [i, num/i]
            if num/i == i: del divisors[-1]
        i += 1
    return sum(divisors)


amicablenumbers = []
for num in range(10, 10000):
    divisorsum = sumofdivisors(sumofdivisors(num))
    if num == divisorsum and sumofdivisors(num) != num:
        if num not in amicablenumbers: amicablenumbers.append(num)
        if divisorsum not in amicablenumbers: amicablenumbers.append(divisorsum)

print sum(amicablenumbers)
