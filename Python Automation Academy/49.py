'''

File Operations

'''

# a
f=open("text_for_49.txt","r")
file_content = f.read()
print(file_content)
f.close()

# b
f=open("text_for_49.txt","w")

f.write('dasdasfdsaf\ndfdgd\nsfsfsf\nsdfsfs\nsfsagfsfd')

f.close()

# c
f=open("text_for_49.txt","a+")

f.write('dasdasfdsaf\ndfdgd\nsfsfsf\nsdfsfs\nsfsagfsfd')

f.close()

