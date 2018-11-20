
# x = int(input("Please enter a number: "))

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except :
#         print("Oops!  That was no valid number.  Try again...")

# print('goodbye')


try:
    number = int(input('Enter number: '))
    result = number/0
except ValueError:
    print("enter in a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print('something bad happended')
finally:
    print('closing statement')