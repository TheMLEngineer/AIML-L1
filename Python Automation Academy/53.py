f = open('ex1.txt' , 'a+')

f.fileno()

f.flush()

f.isatty()

f.close()

#f.detach()

f = open('ex1.txt' )

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

f = open('ex1.txt' , 'w+')

f.truncate()

f.write('Hello')

f.close()
