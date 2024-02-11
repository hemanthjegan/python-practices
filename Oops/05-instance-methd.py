class student:
    name = "raja"
    age = 25

    def printall(self):  # self means instance key or parameter
        print(student.name)
        print(student.age)


    def printall2(self, gender):  # self means instance method
        print(student.name)
        print(student.age)
        print(gender)

o = student()

o.printall()
student.printall(o)

o.printall2("male")
student.printall2(o, "male")

