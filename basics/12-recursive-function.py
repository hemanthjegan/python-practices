def emptyBlock (x):
    pass

emptyBlock(5)

def factorial(x):
    if(x == 1):
        return 1
    else:
        return (x*(factorial(x-1)))

print(factorial(5))
