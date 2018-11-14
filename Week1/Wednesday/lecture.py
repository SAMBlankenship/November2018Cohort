# # my list

# myShoppingList = ["apples", "kale", "ginger", "spinach"]

# #apples
# myShoppingList[0]

# #kale
# myShoppingList[1]

# #ginger
# myShoppingList[2]

# #spinach
# # myShoppingList[3]


# print(myShoppingList[0])

# myShoppingList[0] = "celery"

# print(myShoppingList[0])
# l = len(myShoppingList)
# print(l)

# myShoppingList.append("oranges")

# l = len(myShoppingList)
# print(l)



# print(myShoppingList)


# numbers = [1, 2, 3, 4, 5, 8]

# numbersSubet = numbers[0:2]
# # print(numbers[0:2])

# print(numbersSubet[0])

# print(numbers[4:5])

# numbersSubet = numbers[4:5]

# print(len(numbersSubet))

# print(numbersSubet[0])

# numbers = [1, 2, 3, 4, 5, 8]
# print(len(numbers))
# numbers.insert(1, 56)

# print(len(numbers))


# numbers = [1, 2, 3, 4, 5, 8]

# numbers.append([44, 6, 8])

# print(numbers)


# numbers = [22, 2, 3, 13, 5, 1]
# pv = numbers.pop()

# print(numbers)
# print(pv)
# print(numbers[1])
# print(numbers.index(1))

# numSort = numbers.sort()
# print(numSort)

# newNumbers = numbers.copy()

# print(newNumbers)

# myName = "Hiroko"

# print(len(myName))

# sentence = "this is a wonderful life"

# print(sentence.index(' '))

# numbers1 = [22, 2, 3, 13, 5, 1]

# numbers2 = [2, 23, 33, 131, 52, 13]

# # print(numbers1 + numbers2)

# print(numbers1 * 3)


# myTuple = (1, 3, 5)

# print(myTuple[0])


# myTuple = (1, "Sandhya", "Ram")

# myTuple[0] = "hello"
# print(myTuple)


# myRange = range(10)

# print(myRange)

# for outterIndex in range(1, 11):
#     # print("index:", index)
#     for innerIndex in range(1, 11):
#         print(outterIndex, " x ", innerIndex, " = ", outterIndex * innerIndex )

# president = ['George', 'W', 'Bush']

# print(president)

# for name in president:
#     # print(president.index(name))
#     print("name:" ,name)
#     print("pop:", president.pop())

# print("my list length", len(president))

# print(president)



myRange = range(10)

print(myRange)

for outterIndex in range(1, 11, 2):
    # print("index:", index)
    for innerIndex in range(1, 11, 3):
        print(outterIndex, " x ", innerIndex, " = ", outterIndex * innerIndex )

