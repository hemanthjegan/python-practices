try:
    a = 10/0
except Exception as e:
    print(e)

print("--------------------------------------------------")

try:
    a = 10/0
except Exception as e:
    print(e)
else:
    print("Value of A is : ",a)

print("--------------------------------------------------")

try:
    a = 10/25
except Exception as e:
    print(e)
else:
    print("Value of A is : ",a)

print("--------------------------------------------------")

try:
    a = 10/0
except Exception as e:
    print(e)
else:
    print("Value of A is : ",a)
finally:
    print("Thank you")
    
print("--------------------------------------------------")

try:
    a = 10/25
except Exception as e:
    print(e)
else:
    print("Value of A is : ",a)
finally:
    print("Thank you")