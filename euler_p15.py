#Euler - probelm 15
"""Starting in the top left corner of a 2x2 grid, and only being able to move to the right
and down, there are exactly 6 routes to the bottom right corner. How many such routes
are there through a 20x20 grid?"""

from math import factorial as f

#IDEA: Let moving to right be 'X' and moving down be 'Y'. Number of routes is the number of
# possible length 40 sequences 'XXYXYYXXX...' each with 20 'X's and 20 'Y's
print f(40)/(f(20)*f(20))
