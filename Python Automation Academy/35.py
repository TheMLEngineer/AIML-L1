'''

Tuple 

'''


# a

provided_tuple_1 = ('mon' , 'tue' , 'wed' , 'thur' , 'fri' , 'sat' , 'sun')
print(provided_tuple_1)

# b

provided_tuple_2 = ('January' ,
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

print(tuple(list(provided_tuple_1) + (list(provided_tuple_2))))

# c

provided_tuple_1 = tuple(range(10))
provided_tuple_2 = tuple(range(10,20))
provided_tuple_3 = tuple(range(20,30))

print(max(list(provided_tuple_1) + list(provided_tuple_2) + list(provided_tuple_3)))

# d

print(provided_tuple_1)

provided_tuple_1 = provided_tuple_1[:-1]

print(provided_tuple_1)

del provided_tuple_2


provided_tuple_1 = tuple(list(provided_tuple_1) + [3232])

print(provided_tuple_1)
