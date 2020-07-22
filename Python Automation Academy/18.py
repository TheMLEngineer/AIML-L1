'''

Looping Structures

'''

# a 
list_of_elements_of_a = [] 
for i in range(1,101):
    print(i)
    list_of_elements_of_a.append(i)
print(list_of_elements_of_a[::-1])


# b 
list_of_elements_of_b = []
i = 1
while i <= 100:
    print(i)
    list_of_elements_of_b.append(i)
    i += 1
print(list_of_elements_of_b)

#c
mystring ="Hello world"
for i in mystring:
    print(i)
