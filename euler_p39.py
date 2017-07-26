# Euler - problem 39
"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?"""

from math import sqrt

p = {}
for a in range(1, 1000):
    for b in range(a, 1000):
        c =  sqrt(a**2  + b**2)
        perimeter = a + b + c
        if c == int(c) and perimeter <= 1000:
            if perimeter not in p.keys(): p[perimeter] = 1
            else: p[perimeter] += 1

print [key for key in p.keys() if p[key] == max(p.values())]
