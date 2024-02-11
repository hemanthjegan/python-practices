# name = input("Enter any String:")
# print(name)

# a = int(input("Enter value of A:"))
# b = input("Enter value of B:")
# print(int(b))
# print(type(b))


# name1,name2,name3 = input("Enter 3 names").split()
# print(name1)
# print(name2)
# print(name3)

# multi line string
# a= """ nsicnincincinnnnnnnsknksaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"""
# print(a)

#list
a = ["1","2","3"]
print(','.join(a))  #join not used in int

# getting input for multi line string
para = []
print("enter a para : ")
while True:
    line = input()
    if line:
        para.append(line)
    else:
        break;
print(para)
print("\n".join(para))