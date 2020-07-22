'''

List Operations

'''

list1 = ['Tokyo' , 'Kyoto' , 'Hosu' , 'Osaka' , 'Kobe']
list2 = ['Banglore' , 'Chennai' , 'Mumbai' , 'Delhi' , 'Kolkata']
list3 = ['New York' , 'Kansas City' , 'Chicago' , 'New Jersey' ,'Texas']

# a
for city in list1:
    print(city , len(city))
for city in list2:
    print(city , len(city))
for city in list3:
    print(city , len(city))

# b


def max_in_city(l):
    max1 = ''
    for i in l:
        if len(i) > len(max1):
            max1 = i
    return max1

def min_in_city(l):
    min1 = l[0]
    for i in l:
        if len(i) < len(min1):
            min1 = i
    return min1

print('Max in city 1 : ' , max_in_city(list1))
print('Min in city 1 : ' , min_in_city(list1))
print('Max in city 2 : ' , max_in_city(list2))
print('Min in city 2 : ' , min_in_city(list2))
print('Max in city 3 : ' , max_in_city(list3))
print('Min in city 3 : ' , min_in_city(list3))


# c

l = []

for i in [list1 , list2 , list3]:
    l.extend(i)
    
print('Max of all Cities : ' , max_in_city(l))
print('Min of all Cities : ' , min_in_city(l))
l

# d

list1 = list1[1:-1]
list2 = list2[1:-1]
list3 = list3[1:-1]
print(list1)
print(list2)
print(list3)

