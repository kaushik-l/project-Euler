# Euler - problem 13
"""Work out the first ten digits of the sum of the  one-hundred 50-digit numbers in largesum.txt"""

import sys

f = open(sys.argv[1], 'rU')
print str(sum([int(line) for line in f.readlines()]))[0:10]
