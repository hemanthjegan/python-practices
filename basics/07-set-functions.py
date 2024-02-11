"""
set not usable index beacause it change the position any time
it doesn't allow duplicates
"""

"""

name = {"ram", "raj", "ravi"}
print(name)
print(type(name))

# using for loop access the element
for names in name:
    print(names)

# adding new ele
name.add("suresh")
print(name)

# update another set of data
a={"kumar", "sundar", "vishnu"}
name.update(a)
print(name)

name.remove("ravi")
print(name)

name.discard("sara")  # its used for remove if the element not in tuple it doesnot raise error
print(name)

name.pop()
print(name)

name.clear()
print(name)

del name
# print(name)

a = {'ram', 'ram', 'ravi', 'raj', 'suresh', 'kumar', 'sundar', 'vishnu'}
print(a)  # not allow duplicates

a = {1,2,3,4}
b = {"a", "b","c","d"}
c=a.union(b)
print(c)
a.update(b)
print(a)

a = {1,2,3,4,5,6}
b = (5,6,7,8,9)
c= a.intersection(b)  # common element
print("c = ",c)
a.intersection_update(b)
print("a = ",a)

# symmetric difference
a = {1,2,3,4,5,6}
b = (5,6,7,8,9)
c=a.symmetric_difference(b)
print("c = ",c)
a.symmetric_difference_update(b)
print("a = ",a)

"""

a = {1,2,3,4,5,6}
b = (5,6,7,8,9)

c= a.isdisjoint(b)  # common ele bw two set joint else disjoint
print(c)

a = {5,6,7}
b = (5,6,7,8,9)
c=a.issubset(b)
print(c)

c=a.issuperset(b)
print(c)

















