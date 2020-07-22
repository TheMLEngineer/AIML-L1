'''

All Exceptions

'''

exception_list = ['BaseException' , 'ArithmeticError' , 'Exception' , 'BufferError' , 'LookupError' , 
                 'AssertionError' , 'AttributeError' , 'EOFError' , 'FloatingPointError' , 'GeneratorExit' , 
                 'ImportError' , 'ModuleNotFoundError' , 'IndexError' , 'KeyError' , 'KeyboardInterrupt' , 
                 'MemoryError' , 'NameError' , 'NotImplementedError' , 'OSError' , 'OverflowError' , 
                 'RecursionError' , 'ReferenceError' , 'RuntimeError' , 'StopIteration' , 'StopAsyncIteration']

for exception in exception_list:
    try:
        exec('raise ' + exception)
    except:
        print(exception + ' Has happened')
