import math

def small_and_max(list_1):
    return min(list_1) , max(list_1)

def bubble_sort(arr): 
    n = len(arr) 

    for i in range(n-1): 

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
    return arr


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

# a

def top_2_max_element(l):
    l.sort()
    return l[-2:][::-1]

def small_and_max(list_1):
    return min(list_1) , max(list_1)



def count_treasure(l):
    count = 0
    for i in l:
        if i == 'Treasure':
            count += 1
    return count

def biggest_of_4_numbers(a = 1,b = 2,c = 3,d = 4):
    
    l = []
    l.extend([a , b, c, d])
    l.sort()
    return l[-1]


def tuple_extend_list(tup , lis):
    l = list(tup) + lis
    return tuple(l)


def sqrt(*args):
    l = []
    for arg in args:
        l.append(math.sqrt(arg))
    return l





# c

def substr(st = 'Example:String' , delimiter = ':'):
    return st.split(delimiter)


add = lambda x , y : x + y
sub = lambda x , y : x -y
multiply = lambda x , y : x *y
divide = lambda x , y : x /y
modulus = lambda x , y : x % y
floor = lambda x , y : x // y

def prime(num):
    if num > 1:
        for i in range(2, num): 
         
            if (num % i) == 0: 
                print(num, "is not a prime number") 
                break
        else: 
            print(num, "is a prime number") 
    else:
        print(num, "is not a prime number") 
        
def fib(n): 
    a = 0
    b = 1
    sum = 0
    count = 1
    print("Fibonacci Series: ", end = " ")
    while(count <= n):
        print(sum, end = " ")
        count += 1
        a = b
        b = sum
        sum = a + b
        
        
        
        