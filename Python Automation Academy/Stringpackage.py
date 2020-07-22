s = 'Hello World'

# 1
print(s.capitalize())
print(s.casefold())
print(s.center(24))
print(s.count('h'))
print(s.encode())
print(s.endswith('d'))
print(s.expandtabs())
print(s.find('h'))

# 2
print(s.format())
print('{x}'.format_map({'x' : 3}))
print(s.index('Hello'))
print(s.isalnum())
print(s.isalpha())
print(s.isdecimal())
print(s.isdigit())
print(s.isidentifier())

# 3

print(s.islower())
print(s.isnumeric())
print(s.isprintable())
print(s.isspace())
print(s.istitle())
print(s.isupper())
print(s.join('!'))
print(s.ljust(2))

# 4

print(s.lower())
print(s.lstrip())
print('abc'.maketrans({"a": "123"}))
print(s.partition(' '))
print(s.replace('hello' , 'Your'))
print(s.rfind('rl'))
print(s.rindex('d'))
print(s.rjust(3))

# 5

print(s.rpartition('l'))
print(s.rsplit())
print(s.rstrip())
print(s.split())
print(s.splitlines())
print(s.startswith('Hel'))
print(s.swapcase())
print('a'.translate({97: 'None', 98: None, 99: 105}))
print(s.zfill(5))










str_original = 'Hello World'

bytes_encoded = str_original.encode(encoding='utf-8')


str_decoded = bytes_encoded.decode()


print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)


print("We are the so-called \"Vikings\" from the north.")

print('It\'s alright.')

print("This will insert one \\ (backslash).")

print("Hello\nWorld!")

print("Hello\rWorld!")

print("Hello\tWorld!")

print("\110\145\154\154\157")

print("\x48\x65\x6c\x6c\x6f")