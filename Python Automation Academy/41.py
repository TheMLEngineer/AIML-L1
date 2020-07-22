'''

Date and Time

'''


import calendar
import time
import timeit
import sys
import os
import math

# a
print(calendar.calendar(2016  , w = 3 , l = 1 , c = 10))

# b

calendar.leapdays(1980 , 2025)

# c

year = int(input())

if calendar.isleap(year):
    print('THe Given Year is Leap Year')
else:
    print('The year is not Leap year')

# d

print(calendar.month(2016 , 5))
