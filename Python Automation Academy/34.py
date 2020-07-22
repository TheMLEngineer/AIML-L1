'''

List Manipulations

'''

import numpy as np

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

print(max_list)

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

print(min_list)

# d
print(np.mean(min_list))
