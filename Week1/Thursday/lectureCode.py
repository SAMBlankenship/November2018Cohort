
# def f(x):
#     return 2 * x + 1

# print(f(4))


# from turtle import *


# def square():

#     pencolor('orange')
#     width(10)
#     circle(180)

#     up()
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)
#     down()

#     forward(100)
#     right(90)
#     forward(100)
#     right(90)
#     forward(100)
#     right(90)
#     forward(100)

#     # plot.show()
#     #mainloop()

#     for i in range(5):
#         forward(100)
#         right(144)

#     mainloop()

# square()

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# f_output = []
# g_output = []

# def f(x):
#   return 2 * x + 1
# def g(x):
#   return x + 1

# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))

# print(x_list)
# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close() # start a new plot


# printed_hello = False

# def display_hello():
#   print('Hello')
#   printed_hello = True
#   print("insde of function: " + str(printed_hello))

# print("before function gets called: " + str(printed_hello))

# display_hello()

# print("after function gets called: " + str(printed_hello))


words = ['hello', 'world']
def display_list (newArray):
  words[0] = "changed"
  #wordsCopy = words.copy()
  #wordsCopy[1] = "Veronica"
  print(words)
display_list(words)

print(words)