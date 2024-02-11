class student:
    name = "raja"
    age = 25

    def printall():
        print(student.name)
        print(student.age)

student.printall()
print(student.__dict__)

print(getattr(student, "printall"))
getattr(student, "printall")()

print(student.__dict__["printall"])

student.__dict__["printall"]()