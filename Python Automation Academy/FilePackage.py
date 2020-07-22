# a
f=open("test.txt","r")
file_content = f.read()
print(file_content)
f.close()

# b
f=open("test.txt","w")

f.write('dasdasfdsaf\ndfdgd\nsfsfsf\nsdfsfs\nsfsagfsfd')

f.close()

# c
f=open("test.txt","a+")

f.write('dasdasfdsaf\ndfdgd\nsfsfsf\nsdfsfs\nsfsagfsfd')

f.close()


# a

f=open("test.txt","r")
file_content = f.read(10)
print(file_content)
print('\n\n\n\n')
print(f.tell)
f.seek(10)
print(f.read())
f.close()


# b


f=open("test.txt","r")
f.seek(100)
f.close()

# c

f=open("test.txt","r")
l = f.readlines()
#print(l[2])

for i in l[5:]:
    print(i)

f.close()




f = open('example.txt' , 'a+')

f.fileno()

f.flush()

f.isatty()

f.close()

f.detach()

f = open('example.txt' )

f.read()

f.readable()

f.seek(0)
f.readline()

f.seek(0)
f.readlines()

f.seekable()

f.tell()

f.writable()

f.close()

f = open('example.txt' , 'w+')

f.truncate()

f.write('Hello')

f.close()

