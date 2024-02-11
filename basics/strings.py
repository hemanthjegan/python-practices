#string and string functions

a="Hemanth raj"
print(a)
print(type(a))
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())

print("The count of letter a is : ",a.count('a'))
#count the letters

print(a.endswith('aj'))

print(a.find('a'))  # find the index
print(a.find('a',4))

print(a.replace('a', 'A'))

b = "karthik"
print(b)
print(b.isalpha())
print(b.isalnum())
print(b.islower())
print(b.isupper())

c = "he\nis\ngood"
print(c)
print(c.splitlines())

d = "Quick brothers"
print(d)
print(d.split(" "))

e = "   maharaja   "
print(e)
print(len(e))
print(e.strip())
print(len(e.strip()))
print(e.lstrip())
print(len(e.lstrip()))
print(e.rstrip())
print(len(e.rstrip()))

#partition
f = '12-05-2022'
print(f)
print(f.partition('-'))