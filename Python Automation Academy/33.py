'''

List Operations

'''

List=[10,20,30,40,50,60,70]

# a
List.append(80)

# b
List.insert(4 , 100)

#c 
List.sort()
print(List)

#d 
List.sort(reverse= True)
print(List)

# e

for i in range(3):
    List.pop()
    
print(List)  
