#Euler - problem 79
"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317. The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
possible secret passcode of unknown length.
"""

import sys

def get_count(count_tuple):
  return len(count_tuple[1])

f = open(sys.argv[1], 'r')
text = f.read()
entries = list(set(text.split('\n')))
letters_in_passcode = list(set(''.join(entries)))

passcode_dict = {}
for letter in letters_in_passcode:
    passcode_dict[letter] = []
for entry in entries:
    if entry[0] not in passcode_dict[entry[1]]:
        passcode_dict[entry[1]].append(entry[0])
    if entry[0] not in passcode_dict[entry[2]]:
        passcode_dict[entry[2]].append(entry[0])
    if entry[1] not in passcode_dict[entry[2]]:
        passcode_dict[entry[2]].append(entry[1])

items = sorted(passcode_dict.items(), key=get_count)
keys = [item[0] for item in items]
print(''.join(keys))