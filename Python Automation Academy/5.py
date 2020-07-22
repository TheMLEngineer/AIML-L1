'''

Get Input from Argument and find max element

'''


import sys
list_of_argument = sys.argv

max_element_in_list = None


list_of_argument.remove('5.py')

new_list = []
for element in list_of_argument: 
    new_list.append(int(element))
    
max_element_in_list = max(new_list)

print('The Maximum number is : ' , max_element_in_list) 
