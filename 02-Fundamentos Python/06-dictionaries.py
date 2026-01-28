user = {
    "name": "Carlos",
    "age": 35,
    "email": "crlsabm18@gmail.com",
    "active": True,
    (19.12, -98.32): "Cancun México"
}

user["name"] = "Arturo"
user["age"] = 27
user["country"] = "México"
#print(user[(19.12, -98.32)])

# values, items, keys

print(user.items())
print(user.values())
print(user.keys())