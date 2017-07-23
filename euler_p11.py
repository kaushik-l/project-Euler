#Euler - problem 11
"""In the 20x20 grid in numbergrid.txt, what is the greatest product of four
adjacent numbers in the same direction (up, down, left, right, or diagonally)"""

# usage: python euler_p11.py numbergrid.txt
import sys

f = open(sys.argv[1], 'rU')
digits = f.read()
numgrid = [map(int, digits.split()[i:i + 20]) for i in range(0, 381, 20)]

#up-down
maxprod = 0
for col in range(0, 20):
    for row in range(0, 17):
        prod = 1
        for i in range(0,4):
            prod = prod*numgrid[row + i][col]
        maxprod = max(maxprod, prod)

#left-right
for row in range(0, 20):
    for col in range(0, 17):
        prod = 1
        for i in range(0,4):
            prod = prod*numgrid[row][col + i]
        maxprod = max(maxprod, prod)

# diagonally - forward slash pattern
for row in range(0, 17):
    for col in range(0, 17):
        prod = 1
        for i in range(0,4):
            prod = prod*numgrid[row + i][col + i]
        maxprod = max(maxprod, prod)

# diagonally - backslash pattern
for row in range(0, 17):
    for col in range(19, 2, -1):
        prod = 1
        for i in range(0,4):
            prod = prod*numgrid[row + i][col - i]
        maxprod = max(maxprod, prod)

print maxprod
