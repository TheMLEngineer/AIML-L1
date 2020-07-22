'''

Exception Handling

'''

def pound_to_kilo(pound):
    assert pound > 0 , 'Pound can only have positive values'
    assert pound < 100 , 'Aseert for values greater than 100'
    
    return pound / 2.2

print(pound_to_kilo(32))
