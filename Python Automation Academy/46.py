'''

Biggest of 4 numbers function

'''

def biggest_of_4_numbers(a = 1,b = 2,c = 3,d = 4):
    
    l = []
    l.extend([a , b, c, d])
    l.sort()
    return l[-1]

print(biggest_of_4_numbers(21,45,32,2131))
print(biggest_of_4_numbers())
