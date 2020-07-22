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