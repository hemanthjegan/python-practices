class user:
    course = 'Python'


ob = user()  # creating object for class
print(user.__dict__)
print(ob.__dict__)
print(ob.course)

ob.course = "java"
print(ob.__dict__)
print(ob.course)

ob2 = user()
print(ob2.course)