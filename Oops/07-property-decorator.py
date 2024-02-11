class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.msg = self.name+' is '+ str(self.age)+' years old'

    @property   # it convert the function as property ie msg() --> msg
    def msg(self):
        return self.name+' is '+ str(self.age)+' years old'

o = user("raja", 22)
print(o.name)
print(o.age)
print(o.msg)
o.age= 30
print(o.msg)