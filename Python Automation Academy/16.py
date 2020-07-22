'''

Prime  Numbers

'''

given_number = 11
  
if given_number > 1: 
      
    for i in range(2, given_number): 
         
        if (given_number % i) == 0: 
            print(given_number, "is not a prime number") 
            break
    else: 
        print(given_number , "is a prime number") 
else:
    print(given_number , "is not a prime number") 


lower_limit = int(input("Enter lower range: "))  
upper_limit = int(input("Enter upper range: "))  
  
for number in range(lower_limit , upper_limit + 1):
    if number > 1:  
        for i in range(2,number):  
            if (number % i) == 0:  
                break  
        else:  
            print(number)  
