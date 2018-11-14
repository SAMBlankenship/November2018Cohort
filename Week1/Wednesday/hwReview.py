
day = 0

while (day != -1):

    day = int(input("Enter in day of week: (0-6)"))

    if( day >=6):
        print('numbers must between 0 an 6')
    elif( day < -1):
        print('numbers must between 0 an 6')
    elif (day == 0):
        print('Sunday')
    elif(day ==1):
        print('Monday')
    elif(day ==2):
        print('Tuesday')
    elif(day ==3):
        print('Wednesday')
    elif(day ==4):
        print('Thursday')
    elif(day ==5):
        print('Friday')
    elif(day ==6):
        print('Saturday')

print('goodbye')