days = int(input("enter the days : "))
if (days == 0):
    print("No fine")
elif (days >= 1 and days <= 5):
    print("fine : ", days * 0.5)
elif (days >= 5 and days <= 10):
    print("fine : ", days * 1)
elif (days >= 10 and days <= 30):
    print("fine : ", days * 5)
else:
    print("membership cancelled")
