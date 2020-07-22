'''

Functions

'''


# a

add = lambda x , y : x + y
sub = lambda x , y : x -y
multiply = lambda x , y : x *y
divide = lambda x , y : x /y

# b

sqrt = lambda x = 9 : math.sqrt(x)

def sqrt(*args):
    l = []
    for arg in args:
        l.append(math.sqrt(arg))
    return l

print(sqrt(2,3,4,65))

# c

def substr(st = 'Example:String' , delimiter = ':'):
    return st.split(delimiter)

print(substr())
