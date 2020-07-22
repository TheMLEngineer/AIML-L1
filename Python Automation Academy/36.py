'''

Tuple functions

'''


# a

tup1 = ('mon' , 'tue' , 'wed' , 'thur' , 'fri' , 'sat' , 'sun')
print(tup1)

# b

tup2 = ('January' ,
'February' ,
'March',
'April' ,
'May' ,
'June' ,
'July' ,
'August',
'September',
'October' ,
'November',
'December')

print(tuple(list(tup1) + (list(tup2))))

# c

tup1 = tuple(range(10))
tup2 = tuple(range(10,20))
tup3 = tuple(range(20,30))

print(max(list(tup1) + list(tup2) + list(tup3)))

# d

tup1

tup1 = tup1[:-1]

print(tup1)

del tup2

tup2

tup1 = tuple(list(tup1) + [3232])

print(tup1)












print(tup3.count(22))

print(tup3.index(23))

print(len(tup3))

print(max(tup3))

print(min(tup3))

print(any(tup3))

print(all(tup3))


