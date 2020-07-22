'''

Dictionary operations

'''

dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}


# a

dict1.update(dict2)

print(dict1)

# b

dict1['Salary'] = dict1['Salary'] + dict1['Salary'] * 10 / 100

print(dict1)

# c

dict1['Age'] = 26

print(dict1)

# d

dict1["grade" ] = 'B1'

print(dict1)

# e

from pprint import pprint

for k , v in dict1.items():
    print(k)
    print(v)

# f

del dict1['Age']

print(dict1)
