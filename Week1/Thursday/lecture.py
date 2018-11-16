


# def sampleFunction():
#     print("hello world")

# sampleFunction()

# def f(x):
#     print(x)


# f("hello world")

# f("digital crafts bootcamp")


# def f(x):
#     return x * x

# myFunctionCall = f(4)

# print(myFunctionCall)

# def g(x):
#     return x + 1


# for index in range(-3, 5):
#     print("f({x})={y} \t g({x})={z}".format(x=index, y=f(index), z=g(index)))


# def f(x):
#     return 2 * x + 1

# def g(x):
#     return x + 1

# for x in range(-3, 5):
#     print("f({x}) = {y} ".format(x=x, y=f(x)))


# def sampleFunction(a, b, c):
#     print("hello world: {a}/{a} {b}/{c} {c}".format(b=b, a=a, c=c))
#     #print(a, b, c)


# sampleFunction(c=3, a=2, b=1)

# sampleFunction(3, 2, 1)

# from math import sqrt

# def quadratic(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c) / (2*a)
#     return (x1 + x2), (x1 - x2)


# print(quadratic(b=93, a=31,  c=62))

# a = [1, 2, 3, 4, 5]

# def someFunction() :
#    newArray = a.copy() 
#    newArray[0] = 234
#    print(newArray)


# someFunction()
# print(a)

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# # xrange = list(range(2, 10))
# # yrange = list(range(2, 10))

# # pyplot.plot(xrange, yrange)

# # pyplot.savefig('samplePlot.png')

# # pyplot.close()

# f_output = []
# g_output = []

# x_list = list(range(-3,5))

# def f(x):
#     return 2 * x + 1

# def g(x):
#     return x + 1

# for x in x_list:
#     f_output.append(f(x))
#     g_output.append(g(x))

# pyplot.plot(x_list, f_output, x_list,g_output )
# pyplot.savefig('myplot.png')
# pyplot.close()


from turtle import *

pencolor('orange')
width(10)
circle(180)

up()
forward(50)
left(90)
forward(50)
left(90)
down()

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
mainloop()

