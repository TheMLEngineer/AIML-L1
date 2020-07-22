'''

Looping Structures?""

'''


# a

print('*' * 100)
for i in range(100):
    if i == 50:
        break
    elif i == 10 or i == 20 or i == 30 or i == 40 or i == 50:
        continue
    elif i % 2 != 0:
        pass
    else:
        print(i)

print('*' * 100)
# b

i = 1
while i <= 100:
    #print(i)
    if i == 90:
        break
    elif  i == 60 or i == 70 or i == 80 or i == 90:
        continue
    elif i % 2 != 0:
        pass
    else:
        print(i)
    i += 1


