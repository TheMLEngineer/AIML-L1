
'''

To find given Number is odd or even

'''
import sys

try:
    given_number = int(input('Please Enter the Number : '))
except:
    print('Please check input type , Provide number type')
    sys.exit('Input type was not int')

try:
    if given_number % 2 == 0 :
        print('Given Number is EVEN')
    elif given_number % 2 != 0 :
        print('Number is ODD')
except:
    print('Exception Happened in Number comparison')
