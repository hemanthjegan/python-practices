import datetime as dt

current_date = dt.date.today()
print("Current Date : ", current_date)

new = dt.date(2002, 12, 5)
print(new)
print("year :", new.year)
print("month :", new.month)
print("date : ", new.day)
print("--------------------------------------------------")

a= dt.time(10, 45, 5, 64566)
print(a)
print("--------------------------------------------------")

current_time = dt.datetime.now()
print(current_time)
print("--------------------------------------------------")

new = dt.datetime(2002,11,16,4,54,34)
print(new)
print(new.date())
print(new.time())
print("--------------------------------------------------")

current = dt.datetime.now()
nxtNewYear = dt.datetime(2025,1,1)
diff = nxtNewYear-current
print(diff)
print("--------------------------------------------------")

current = dt.datetime.now()
print(current)
s=current.strftime("%A %B %d %Y")
print(s)













