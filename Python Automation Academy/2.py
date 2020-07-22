'''

Biggest of three numbers

'''
list_of_3_numbers = []

for i in range(3):
    try:
        list_of_3_numbers.append(int(input('Please Enter Number ' + str(i) + ' For Comparison : ')))
    except:
        pass
    

max_of_three_numbers = None

try:
    if list_of_3_numbers[0]> list_of_3_numbers[1] and list_of_3_numbers[0] > list_of_3_numbers[2]:
        max_of_three_numbers = list_of_3_numbers[0]
    elif list_of_3_numbers[1]> list_of_3_numbers[0] and list_of_3_numbers[1] > list_of_3_numbers[2]:
        max_of_three_numbers = list_of_3_numbers[1]
    else:
        max_of_three_numbers = list_of_3_numbers[2]
    print('The Maximum number is : ' , max_of_three_numbers)
    
except:
    print('Please check the data type you enter , Is the input value is number type ?')


