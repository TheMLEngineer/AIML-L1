'''

Date and Time Module

'''

# a and b combined while running for first time , finding time as well

import time
import timeit



def one_minute_print():
    count = 0 
    for i in range(12):
        time.sleep(5)
        print(datetime.datetime.now())
        count += 1
        
        
        
begin_time = datetime.datetime.now()



one_minute_print()


print('\n\n\n\nThe Script Execution Time was : ')



print(datetime.datetime.now() - begin_time)
