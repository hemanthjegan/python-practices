class student:
    def __init__(self, total):
        self._total = total  # private variable

    def average(self):
        return self._total / 5.0

    def getter(self):
        return self._total

    def setter(self, t):
        if t<=0 or t>=500:
            print("Invalid total and can't change")
        else:
            self._total = t

    total = property(getter, setter)

ob = student(470)
print("total :", ob.total)
print("average : ", ob.average())
ob.total = 360
print("total :", ob.total)
print("average : ", ob.average())