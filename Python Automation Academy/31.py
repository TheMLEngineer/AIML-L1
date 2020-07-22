'''

Binary Search

Dependency Library install : pip install algorithms

'''

from algorithms import search

given_list = [1,2,3,4,5]

number_to_search = int(input('Enter the Number to search : '))
if search.binary_search(given_list , number_to_search) is None:
    print('Provided Number is not present in list')
    print('Unsuccessful')
else:
    print('privided number is present in index : ' ,search.binary_search(given_list , number_to_search) )
    print('Successful')
