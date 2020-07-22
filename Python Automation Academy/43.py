'''

Search element in list using custom function

'''

def search_in_list(l , len_l , search_element):
    for i in range(len_l):
        if search_element == l[i]:
            return 'Element Found : ' + str(l[i]) + "\nAt Index : " + str(i)
        

print(search_in_list([1,2,3,4,5] , 5 , 3))
