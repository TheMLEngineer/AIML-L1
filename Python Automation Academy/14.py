'''

List Functions and Methods

'''


list_a = list(range(0,10))
list_b = ['Liam',
'Noah',
'William',
'James',
'Oliver',
'Benjamin',
'Elijah',
'Lucas',
'Mason',
'Logan']

# a
print('=' * 50)
print(list_b)
print('=' * 50)
# b 
for i in list_a:
    print(list_b[i])
print('=' * 50)
# c 
print(list_b[3:10])
print('=' * 50)
# d
print(list_b[2:])
print('=' * 50)
# e 
n = int(input('Enter How many times you wanna print repeated list'))
print(list_b * n)
print('=' * 50)
# f 

l = []
l.append(list_a)
l.append(list_b)
print(l)
print('=' * 50)
# g 

print(list_a[0] , list_b[0])
print('=' * 50)
