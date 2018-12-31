#Euler - problem 67
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.
< data in triangle2.txt >
"""

import sys

f = open(sys.argv[1], 'r')
text = f.read()
f.close()
lines = text.split('\n')
levels = []
for indx, line in enumerate(lines):
    levels.append([int(item) for item in line.split(' ')])

for levelnumber in range(len(levels)-2, -1, -1):
    for indx in range(len(levels[levelnumber])):
        levels[levelnumber][indx] += max(levels[levelnumber+1][indx], levels[levelnumber+1][indx+1])

print(levels[0])