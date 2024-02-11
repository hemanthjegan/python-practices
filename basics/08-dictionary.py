"""
dictionary :
{key : values}
key is unique
"""
user = {
    "name" : "raj",
    "age" : 21,
    "isMarried" : False
}

print(user)
print(type(user))
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x," ",user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x, y in user.items():
    print(x, y)

if "age" in user:
    print("found")
else:
    print("not found")

# changing values
user.update({"gender" : "male"})
print(user)

user["age"] = 22;
print(user)

user.pop("age")
print(user)

user.clear()
print(user)

users = {
    "user1" : {
        "name" : "raj",
        "age" : 21,
        "isMarried" : False
    },
    "user2" : {
        "name" : "raj",
        "age" : 21,
        "isMarried" : False
    }
}

print(users)