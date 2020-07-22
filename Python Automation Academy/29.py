'''

Built IN String Functions Python

'''

given_string = 'Hello World'

# 1
print(given_string.capitalize())
print(given_string.casefold())
print(given_string.center(24))
print(given_string.count('h'))
print(given_string.encode())
print(given_string.endswith('d'))
print(given_string.expandtabs())
print(given_string.find('h'))

# 2
print(given_string.format())
print('{x}'.format_map({'x' : 3}))
print(given_string.index('Hello'))
print(given_string.isalnum())
print(given_string.isalpha())
print(given_string.isdecimal())
print(given_string.isdigit())
print(given_string.isidentifier())

# 3

print(given_string.islower())
print(given_string.isnumeric())
print(given_string.isprintable())
print(given_string.isspace())
print(given_string.istitle())
print(given_string.isupper())
print(given_string.join('!'))
print(given_string.ljust(2))

# 4

print(given_string.lower())
print(given_string.lstrip())
print('abc'.maketrans({"a": "123"}))
print(given_string.partition(' '))
print(given_string.replace('hello' , 'Your'))
print(given_string.rfind('rl'))
print(given_string.rindex('d'))
print(given_string.rjust(3))

# 5

print(given_string.rpartition('l'))
print(given_string.rsplit())
print(given_string.rstrip())
print(given_string.split())
print(given_string.splitlines())
print(given_string.startswith('Hel'))
print(given_string.swapcase())
print('a'.translate({97: 'None', 98: None, 99: 105}))
print(given_string.zfill(5))
