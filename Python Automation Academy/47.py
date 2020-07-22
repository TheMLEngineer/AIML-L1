'''

Extend Tuple with List

'''

def tuple_extend_list(tup , lis):
    l = list(tup) + lis
    return tuple(l)

print(tuple_extend_list((1,2,3) , [5,6,7]))
