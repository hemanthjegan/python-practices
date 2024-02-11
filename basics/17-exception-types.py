# types exception
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# name error exception
try:
    print(a)
except NameError as e:
    print("A is not defines")

# ZeroDivisionError exception
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Denominator cannot be zero")

# ValueError exception
try:
    a = int("raja")
except ValueError as e:
    print("Enter numbers only")

# IndexError exception
try:
    a = [1, 2, 3, 4, 5]
    print(a[10])
except IndexError as e:
    print("Invalid index")

# FileNotFoundError exception
try:
    f = open("text.txt")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
