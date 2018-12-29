#Euler - problem 42
"""
The nth term of the sequence of triangle numbers is given by, t_n = 0.5*n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word. Using
words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import sys
from math import sqrt

def word2num(word):
    return sum([(alphabet.find(char) + 1) for char in word])

def istrianglenum(num):
    return int(sqrt(2*num))*(int(sqrt(2*num)) + 1) == 2*num

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open(sys.argv[1], 'r')
text = f.read()
wordlist = [word[1:-1] for word in text.split(',')]
numtrianglewords = 0
for word in wordlist:
    numtrianglewords += istrianglenum(word2num(word))

print(numtrianglewords)