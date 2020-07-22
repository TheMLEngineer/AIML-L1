'''

Vowel Count

'''

given_string = "This is Python"

string = given_string.casefold() 

count = {}.fromkeys('aeiou', 0) 

for character in string: 
    if character in count: 
        count[character] += 1    
print(count )
