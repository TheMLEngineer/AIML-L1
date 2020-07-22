import numpy as np

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

print(list1[1:-1])
print(list2[1:-1])
print(list3[1:-1])









list1 = ['Tokyo', 'Kyoto', 'Hosu', 'Osaka', 'Kobe']
list1

# a
list1.append('San Fransisco')
list1

# b
list1.insert(4 , 'Hi')

list1

# c
list1.sort()
print(list1)

# d
list1.sort(reverse=True)
print(list1)

# e
for i in range(3):
    list1.pop()
    
list1


list1 = list(range(10))
list2 = list(range(10 , 20))
list3 = list(range(20 , 30))

# a

def top_2_max_element(l):
    l.sort()
    return l[-2:][::-1]

max_list = []
for l in [list1 , list2 , list3]:
    print('1st max , 2nd Max')
    print(top_2_max_element(l))
    max_list.extend(top_2_max_element(l))

max_list

# b

print(np.mean(max_list))

# c


def bottom_2_max_element(l):
    l.sort(reverse = True)
    return l[-2:][::-1]

min_list = []
for l in [list1 , list2 , list3]:
    print('1st min , 2nd min')
    print(bottom_2_max_element(l))
    min_list.extend(bottom_2_max_element(l))

min_list

# d
print(np.mean(min_list))