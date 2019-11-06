x = 1   # global variable

def local():
    x = 0
    print(x)    # local variable

print(x)    # this prints the global variable x which is equal to 1
            # it prints 1 because it is a global variable which means
            # it was created outside of the function

local()     # this prints the local variable x which is equal to 0
            # it does this because it is a local variable which means it
            # can only be accessed inside a function
