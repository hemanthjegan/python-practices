class student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def printall(self):
        print("name : ", self.name, " age : ", self.age)

    @classmethod  # it acces the class property, cls is defined as a class property
    def totalAdmission(cls):
        return cls.count


o = student("raja", 22)
o.printall()
print("total admission : ", o.totalAdmission())

o = student("joes", 21)
o.printall()
print("total admission : ", student.totalAdmission())
