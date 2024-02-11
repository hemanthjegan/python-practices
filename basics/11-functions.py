# 9 types of functions

def func():
    print("Welcome to function topic")


func()


# no return type without argumnet function
def add():
    a = 2
    b = 4
    print("c = ", a + b)


add()


# no return type with argumnet function
def sub(a, b):
    print("c = ", a - b)


sub(9, 3)


# return type without argumnet function
def mul():
    a = 2
    b = 4
    c = a * b
    return c


print("c = ", mul())


# return type with argumnet function
def div(a, b):
    c = a / b
    return c


print("c = ", div(9, 3))


# arbitrary function
def classA(*students):
    print(students)
    for user in students:
        print(user)


classA("ram", "raj", "ravi")


# keyword arguments function
def msg(name, age):
    print(name, "age is", age)


msg(age=22, name="raja")  # keywords


# arbitrary keyword arguments function
def bio(**data):
    print(data)
    for user in data.values():
        print(user)


bio(name="ram", gender="male", age=22)


# default parameter function
def user(name, city="salem"):  # salem default value
    print(name, "is from", city)


user("raja", "KOVILPATTI")
user("ram")

# passing list as an argument
def total(marks):
    return sum(marks)

print(total([78,68,97,85,89,70]))
