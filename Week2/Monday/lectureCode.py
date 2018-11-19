
# class Student:
#     def __init__(self, firstN, lastN):
#         self.firstName =  firstN
#         self.lastName = lastN

#     def GreetStudent(self):
#         print(f"Hello {self.firstName}  {self.lastName}")
#     def Greeting(self, person):
#         print("hello world " + person)

# Shoba = Student("Shoba", "Boddapati")

# Shoba.GreetStudent()
# Shoba.firstName = "Shob"

# Shoba.GreetStudent()

# Hiroko = Student("Hiroko", "Ross")

# Hiroko.GreetStudent()




# Shoba = Student.Greeting("Hiroko")

# Hiroko = Student.Greeting("Shoba")

class Car:
    greeting = "hello world"
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def ChangeColor(self,toColor):
        print(f"Chaning from {self.color} to {toColor}")
        self.color = toColor
        print(f"New color is {self.color}")

    def openDoor(self):
        print("open door")

    def displayColor(self):
        print(f"The color of the car is {self.color}")
        return self.color

    @classmethod
    def instanceMethod(cls):
        print(f"this an instance")

    
    def instanceMethod1(self):
        print(f"this an instance {self.color} ")

class ElectricCar(Car):
    def __init__(self, make, model, range, autopilot):
        super().__init__(make, model, "red")
        self.range = range
        self.autopilot = autopilot

    def batteryLife(self, life):
        print(f"battery life is: {life}")

class Hybrid(Car):
    def __init__(self, make, model, color, batterLife):
        super().__init__(make, model, color)
        self.batterLife = batterLife

        


myHybrid = Hybrid("toyota", "prius", "silver", "2 hours")

myHybrid.ChangeColor("lime")
    
# tesla = ElectricCar("tesla", "model s", "3 hours", "yes")

# print(tesla.displayColor())

# tesla.batteryLife("3 hours")


# car = Car("Toyota", "Tundra", "Red")
# car.instanceMethod1()

# car2 = Car("Honda", "Civic", "Blue")
# car2.instanceMethod()

# car = Car("Toyota", "Tundra", "Red")

# car.ChangeColor("green")

# print(car.greeting)
# # print(car.color)

# car.openDoor()
# car.displayColor()

# car2 = Car("Honda", "Civic", "Blue")
# print(car2.greeting)



