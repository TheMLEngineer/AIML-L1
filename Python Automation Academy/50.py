'''

File Operations

'''

# a

f=open("text_for_50.txt","r")
file_content = f.read(10)
print(file_content)
print('\n\n\n\n')
print(f.tell)
f.seek(10)
print(f.read())
f.close()

# b


f=open("text_for_50.txt","r")
f.seek(100)
f.close()

# c

f=open("text_for_50.txt","r")
list_of_content = f.readlines()
#print(l[2])

for i in list_of_content[5:]:
    print(i)

f.close()


print(list_of_content)
