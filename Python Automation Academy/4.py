'''

To find Given Number is Prime or Not

'''
import sys

try:
    given_number = int(input('Please Enter the number : '))
except:
    print('Please check input type , Provide number type')
    sys.exit('Input type was not int')

if given_number > 1: 
      
    for i in range(2, given_number): 
         
        if (given_number % i) == 0: 
            print(given_number , "is not a prime number") 
            break
    else: 
        print(given_number, "is a prime number") 
else:
    print(given_number, "is not a prime number") 
