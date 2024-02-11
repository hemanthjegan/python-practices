"""
list is sequence type
mutable (changeable)

"""

a=[1,2,3,4,5]
print(a)
print(type(a))
a[0] = 10
print(a)
print("------------------")

print("slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print((a[2:]))
print((a[:3]))
print("------------------")

a=[1, True, 'raj', 2.45]
print(a)
print("------------------")

a=[1, True, 'raj', 2.45, [5,6,7,8,9,10]]
print(a)
print(a[4][3])
print("------------------")

a=[10,20,30,40,50]
print(a)
a.clear()
print(a)

a=[10,20,30,40,50]
b=a.copy()
print(b)

a=[90,20,30,90,50,60,50,20,90]
print(a)
print(a.count(90))
print(len(a))

a=[10,20,30,40,50]
print(a.index(40))
print(max(a))
print(min(a))

a=[10,20,30,40,50,40]
a.pop(1)  # remove element using index
print(a)
a.remove(40)  # remove element using element
print(a)
print("------------------")

names = ["raja"]
names.append("ravi")
names.append("kaumar")
print(names)

name2=["sara", "anitha"]
names.extend(name2)
print(names)

names.insert(0, "surya")
print(names)
print("------------------")

# list constructor
print(list(range(5)))
print(list("Hemanth raj"))

a = [5,89,35,83,62,6,35,114,45,29,67,185]
print(a)
a.sort()
print(a)
# a.reverse()
a.sort(reverse=True)
print(a)

a = ["orange", "apple", "guava"]
print(a)
a.sort()
print(a)
# a.reverse()
a.sort(reverse=True)
print(a)
a.sort(key=len)  # sort based on ele length
print(a)
