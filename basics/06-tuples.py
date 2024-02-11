"""
tuple is immutable (not changeable)
surrounded by round brackets ()
"""
a = (1, 2.3, True, "raja")
print(a)
print(type(a))
print(a[2])
print(a[-1])
print(a[0:2])

# convert tuple to list
b = list(a)
print(b)
b.append("ram")
print(b)
print(type(b))

# convert list to tuple
a = tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if "raja" in a:
    print("found")
else:
    print("ot found")

print(len(a))

a = (1)
print(type(a))

a = (1,)
print(type(a))

# we cannot del an element or modify in the tuple but del the entire tuple
del a
# print(a)

a = (1, 2, 3, 4, 6, 5, 6)
b = (5, 6, 7, 8, 9)
c = a + b
print(c)
print(c.count(6))

# nested tuples
a = (1, 2, 3, 4)
b = (5, 6, 7, 8, 9)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][2])
print(c[1][3])

x= ("raja",) * 10
print(x)

a = (5, 9, 7, 8, 6)
print(min(a))
print(max(a))