'''

Palindrome

'''


string_1 = input('Enter String : ')
string_1_reverse = string_1[::-1]
if string_1 == string_1_reverse:
    print('Given string is palindrome')
else:
    print('The string is not a palindrome')
