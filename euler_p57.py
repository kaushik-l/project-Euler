# Euler - problem 57
"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first
example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

def nextfrac(frac):
    return (frac[1], 2*frac[1] + frac[0])

def numislonger(frac):
    return len(str(frac[0] + frac[1])) > len(str(frac[1]))

count, hits = 0, 0
frac = (1, 2)
while count<1000:
    hits += numislonger(frac)
    frac = nextfrac(frac)
    count += 1

print(hits)
