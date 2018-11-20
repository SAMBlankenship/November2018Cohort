
# myContactList = {
#     "first_name" : "Veronica",
#     "last_name" : "Lino",
#     "age" : 12,
#     12: "street",
#     "friends": {
#         "first_name": "Oscar",
#         "last_name" : "Miranda",
#         "occupation" : "student"
#     }
# }


# for key, value in myContactList.items():
#     print("{key}: {value}".format(key=key, value=value))
# del myContactList["age"]

# print(myContactList.keys())
# print(myContactList.values())
# newDictionary = myContactList

# newDictionary["first_name"] = "Shobba"

# print(newDictionary["first_name"])
# print(myContactList["first_name"])

#first_name = myContactList["dog"]

# first_name = myContactList.get("dog")
# print(first_name)

# isItThere = "dog" in myContactList
# print(isItThere)

# if ("dog" in myContactList):
#     print(myContactList["last_name"])

# myList = ["one", "two", "three"]

# myList[0] = 1

# print(myList)

#print(myContactList["age"])

# myContactList["age"] = 18

#print(myContactList["age"])

# def myFunction():
#     myContactList["age"] = 20


# myFunction()
# print(myContactList["age"])

contact = [
    {"first_name": "Veronica",
     "last_name": "Lino",
     "email": "vernica@dc.com",
     "phone": {
         "home": "333-333-3333",
         "cell": "222-222-2222"
        }
    },
    {"first_name": "Shobba",
     "last_name": "Boddapati",
     "email": "me@me.com",
     "phone": {
         "home": "444-444-4444",
         "cell": "555-555-5555"
        }
    },
    {"first_name": "Oscar",
     "last_name": "Miranda",
     "email": "me2@me.com",
     "phone": {
         "home": "666-666-6666",
         "cell": "777-777-7777"
        }
    }
]

result = contact[2]["first_name"]  + " " + contact[2]["phone"]["cell"]

print(result)

