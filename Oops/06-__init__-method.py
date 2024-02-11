# in python constructor is called as __init__ method

class user:
    def __init__(self,name):
        print("call when new instance created")
        self.name = name

    def printall(self):
        print("Name : ", self.name)

ob = user("raja")
ob.printall()
# user.printall(ob)
print(ob.__dict__)

ob2 = user("ravi")
ob2.printall()
print(ob2.__dict__)
print(user.__dict__ )






