
# file_handler = open('lorem.txt', 'r')

# content = file_handler.read()

# file_handler.close()

# print(content)

# file_handler = open('readFile.txt', 'w')

# file_handler.write('i love ramen.  we had a great lunch')

# file_handler.close()

# file_handle = open('lorem.txt', 'r')
# contents = file_handle.readlines()
# file_handle.close()
# print(contents)

# file_handle = open('lorem.txt', 'r')
# line1 = file_handle.readline()
# file_handle.close()
# print(line1)


# file_handle = open('lorem.txt', 'r')
# while True:
#   char = file_handle.read(1)
#   if char is None:
#     break
#   else:
#     print(char)
# file_handle.close()

# file_handle = open('lorem.txt', 'a')
# file_handle.write('Hello World\n')
# file_handle.close()

import pickle

# data = {'name': 'Paul'}

# with open('data.pickle', 'wb') as fh:
#   pickle.dump(data, fh)

# with open('data.pickle', 'rb') as fh:
#   data = pickle.load(fh)
#   print(data)

import json

# data = {'name': 'Paul'}

# with open('data.json', 'w') as fh:
#   json.dump(data, fh)

with open('data.json', 'r') as fh:
  data = json.load(fh)
  print(data)