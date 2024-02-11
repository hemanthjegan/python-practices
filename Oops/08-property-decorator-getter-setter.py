# _variable_name is a private variable

class student:
    def __init__(self, total):
        self.total = total

    def average(self):
        return self.total / 5.0


o = student(470)
print("total :", o.total)
print("average : ", o.average())

o.total = 360
print("total :", o.total)
print("average : ", o.average())

print("--------------------------------------------------")


class students:
    def __init__(self, total):
        self._total = total  # private variable

    def average(self):
        return self._total / 5.0

    def total(self):
        return self._total


ob = students(470)
print("total :", ob.total())
print("average : ", ob.average())

print("--------------------------------------------------")


class students1:
    def __init__(self, total):
        self._total = total  # private variable

    def average(self):
        return self._total / 5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, t):
        if t<=0 or t>=500:
            print("Invalid total and can't change")
        else:
            self._total = t

ob1 = students1(470)
ob1.total = 360
print("total :", ob1.total)
print("average : ", ob1.average())
