'''

Smallest and Largest Using Function

'''

def small_and_max(list_1):
    return min(list_1) , max(list_1)

list_of_elements = []
length_of_list = int(input('Length of List : '))
print('Enter List elements')
for i in range(length_of_list):
    list_of_elements.append(int(input()))
print('Smallest and Largest Is : ' , small_and_max(list_of_elements))
