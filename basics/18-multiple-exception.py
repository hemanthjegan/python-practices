try:
    a=10/20
    print(a)
    b=[1,2,3,4,5]
    print(b[10])
except ZeroDivisionError:
    print("Denominator cannot be zero")
except IndexError:
    print("Invalid index")