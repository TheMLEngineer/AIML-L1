

'''

Multiple File Searching Operations

'''

d = {}
for file in ['ex1.txt' , 'ex2.txt' , 'ex3.txt' , 'ex4.txt']:
    f = open(file)
    f_content = f.read()
    print(f_content.split())
    d[file] = f_content.split()
    f.close()

def count_treasure(l):
    count = 0
    for i in l:
        if i == 'Treasure':
            count += 1
    return count


for key in d.keys():
    d[key] = count_treasure(d[key])
    
print(d)

for k , v in d.items():
    print('The file : ' + k + ' has ' + str(v) + ' times treasure mentioned')
