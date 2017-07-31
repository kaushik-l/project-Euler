# Euler - problem 35
"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?"""

# don't need the actual words, just the letter count
firstdigits = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
seconddigits = {'0': 0, '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}
specialdigits = {'10': 3,'11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8,
                        '100': 7, '1000': 8, 'and': 3}

total = 0
for num in range(1, 1001):
    if num < 10:
        total += firstdigits[str(num)]
        continue
    if num >= 10 and num <= 19:
        total += specialdigits[str(num)]
        continue
    else:
        digits = [digit for digit in str(num)]
        if len(digits) == 2:
            total += seconddigits[digits[0]] + firstdigits[digits[1]]
        elif len(digits) == 3:
            total += specialdigits['100'] + firstdigits[digits[0]]
            if digits[1] == '1':
                total += specialdigits["".join(digits[1:])]
            else:
                total += seconddigits[digits[1]] + firstdigits[digits[2]]
            if not digits[1] == digits[2] == '0': total += specialdigits['and']
        elif len(digits) == 4:
            total += specialdigits['1000'] + firstdigits[digits[0]]

print total
