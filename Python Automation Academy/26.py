'''

Encoding and Decoding

'''

str_original = 'Hello World'

bytes_encoded = str_original.encode(encoding='utf-8')


str_decoded = bytes_encoded.decode()


print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)
