#Euler - problem 9
"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52. There exists exactly one Pythagorean triplet for which
a + b + c = 1000. Find the product abc."""

#IDEA: a^2 + b^2 = c^2 and a + b + c = 1000 => 2e3(a + b) - 2ab = 1e6
for a in range(1, 1000):
    for b in range(a + 1, 1000):
        if 2e3*(a + b) - 2*a*b == 1e6: break
    else: continue
    break

print a*b*(1000 - (a + b))
