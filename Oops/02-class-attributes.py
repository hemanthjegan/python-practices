class student():
    name = "raja"
    age = 21

# get attribute method getattr()
print(getattr(student, "name"))
print((getattr(student, 'age')))
print(getattr(student, 'gender', 'no such attribute'))

# dot notaion
print(student.name)
print(student.age)

# set attribute method setattr()
setattr(student, 'name', 'maharaja')
print(student.name)

setattr(student, 'gender', 'male')
print(student.gender)

student.city = 'kovilpatti'
print(student.city)

print(student.__dict__)

delattr(student, 'city')
print(student.__dict__)

del student.gender
print(student.__dict__)