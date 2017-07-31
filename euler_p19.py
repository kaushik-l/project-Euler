#Euler - problem 19
"""You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible
by 400. How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901
to 31 Dec 2000)?"""

def isLeap(year):
    if (year % 100 == 0 and year % 400 != 0) or (year % 4 != 0): return False
    else: return True

nonleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1901
day = 2                             #Monday = 1, Tue = 2, ...
sundays_on_first = 0
while year < 2001:
    if isLeap(year):
        for days in leap:
            if day % 7 == 0: sundays_on_first += 1
            day += days
    else:
        for days in nonleap:
            if day % 7 == 0: sundays_on_first += 1
            day += days
    year += 1

print sundays_on_first

""" Solution to  number of Sundays in the month of January:
year = 1900
day = 1                                 #Monday = 1, Tue = 2, ...
nSundays = 0
while year < 2001:
    for date in range(1, 32):
        if day % 7 == 0: nSundays += 1
        day += 1
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0: day += 334
        else: day += 335
    else: day += 334
    print year, nSundays
    year += 1

print nSundays
"""
