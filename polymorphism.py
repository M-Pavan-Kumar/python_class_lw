# # function overloading

# def add(a,b=0,c=0):
#     return a+b+c
# print(add(10))
# print(add(10,20))
# print(add(10,20,30))

# def display(*args):
#     for i in args:
#         print(i)

# display(5)
# display(5,10)
# display(5,10,15)

# # operator overloading
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
#     def __sub__(self,other):
#         return self.pages-other.pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
# print(b1-b2)

# # method overriding
# class Vehilcle:
#     def mileage(self):
#         print("General mileage")
# class Car(Vehilcle):
#     def mileage(self):
#         print("Car: 20 km/l")
# class Bike(Vehilcle):
#     def mileage(self):
#         print("Bike: 50 km/l")
    
# # car=Car()
# # car.mileage()
# Car().mileage()
# Bike().mileage()

# for ref in [Car(),Bike()]:
#     ref.mileage()


# Duck Typing

class Idle:
    def execute(self):
        print("Compiling")
        print("Executing")
class Vscode:
    def execute(self):
        print("Running")
        print("Debugging")
def editor(ref):
    ref.execute()

editor(Idle())
editor(Vscode())