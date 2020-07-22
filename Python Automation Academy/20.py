'''

Fibonacci Series

'''


number_of_times_fibonacci =int(input("Enter the number : \t"))
f=0                                         
s=1                                         
if number_of_times_fibonacci <= 0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2, number_of_times_fibonacci ):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
