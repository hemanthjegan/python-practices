class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printall(self):
        print("name : ", self.name, " age : ", self.age)

    @staticmethod
    def welcome():
        print("Welcome to our academy")


o = student("raja", 22)
o.printall()
o.welcome()
