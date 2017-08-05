# Euler - problem 22
"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical position in the list to
obtain a name score. For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714. What is the total of all the name scores in the file?"""

import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open(sys.argv[1], 'rU')
text = f.read()
names = sorted(text.split(','))

namescore = 0
for index, name in enumerate(names):
    namescore += sum([(alphabet.find(char) + 1)*(index + 1) for char in name])

print namescore
