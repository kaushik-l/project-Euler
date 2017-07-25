#Euler - problem 28
"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101. What is the sum of the
numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

#IDEA: diagonal elements are 1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, ...
# therefore, increment the progression by 2 after every four numbers

diagonalnums = [1]
ratio = 0
spiralsize = 1
while spiralsize < 1001:
    spiralsize += 2
    ratio += 2
    diagonalnums += [diagonalnums[-1] + ratio*i for i in range(1, 5)]

print sum(diagonalnums)
