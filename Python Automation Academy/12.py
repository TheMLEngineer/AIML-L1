'''
Comparison Operator

'''

list_of_numbers = []
num = None
for i in range(10):
    num = int(input())
    list_of_numbers.append(num)
    
average = sum(list_of_numbers) / len(list_of_numbers)
less_than_average = []
equal_to_average = []
more_than_average = []

for i in list_of_numbers:
    if i < average:
        less_than_average.append(i)
    if i == average:
        equal_to_average.append(i)
    if i > average:
        more_than_average.append(i)
        
print('less_than_average : ' , less_than_average)
print('equal_to_average : ' , equal_to_average)
print('more_than_average : ' , more_than_average)
