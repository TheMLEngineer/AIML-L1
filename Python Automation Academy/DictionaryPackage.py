dict1 = {1:'Hi' , 2:'Hello' , 3:"hehehe"}
dict2 = {11:'Hi' , 22:'Hiiiii' , 33:"Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"}
dict3 = {111:'Hi' , 222:'yupppppppppppppp' , 333:"Oiiiiiiiiiiiiii"}

for dict_ in [dict1 , dict2 , dict3]:
    count = 1
    max_element = max(dict_.keys())
    count += 1

print(count)

# Biggest key value is in dictionary 3

# b

dict1['new element'] = 'Yipeee'

dict2['new element'] = 'Yellow'

print(dict1)

print(dict2)

# c


print(len(dict1))
print(len(dict2))
print(len(dict3))



# d

print(str(dict1) + str(dict2) + str(dict3))



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