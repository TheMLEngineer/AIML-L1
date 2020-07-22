'''

List Functions and  Methods

'''

list_of_names = ['Liam',
'Noah',
'William',
'James',
'Oliver']
list_of_names_copy = list_of_names.copy()
# a
for i in list_of_names:
    if i == 'James':
        print('James is present in list')

# b

i = 0
while i <= 5:
    try:
        if list_of_names.pop() == 'James':
            print('James is present in list')
    except:
        pass
    i += 1
        
# c 
print(list_of_names_copy[::-1])
