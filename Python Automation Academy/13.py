'''

Decision Making 

'''
import random


number = None
maximum_1 = -99999 
counter = 0
for i in range(5):
    counter += 1
    if counter != 4:
        number = int(input())
    
    #This is logic to extend to find maximum of 5 numbers , This will add number randomly
    number = random.randint(1,3)

    if number > maximum_1:
        maximum_1 = number
print('Max Number : ', maximum_1)  
