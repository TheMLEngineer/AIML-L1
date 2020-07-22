'''

Reverse File content

'''

f = open('text_for_52.txt')
f_content = f.read()
print(f_content)
f.close()


f = open('text_for_52.txt' , 'w')
f.write(f_content[::-1])
f.close()
