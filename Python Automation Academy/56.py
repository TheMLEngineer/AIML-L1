'''

IO Error and Value Error

'''

# a

try:
    raise IOError
except:
    print('IO Error happened , Please check file modes , whether file is opened in proper mode for proper processing')

# b

try:
    raise ValueError
except:
    print('Value Error has happened , please check')
