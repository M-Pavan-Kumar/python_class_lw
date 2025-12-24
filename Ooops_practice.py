# class Student():
#     def display(self):
#         print("I am a student")
# s1=Student()
# s1.display()


# class Laptop():
#     def showBrand(self,brand):
#         print("Laptop brand is : ",brand)
# b1=Laptop()
# b1.showBrand("Asus vivobook")
# b1.showBrand("Samsung")


# Variables in a clsss
# Instance variables : belongs to object
# Class variable : shared by all objects
# class Employee():
#     company="Google"    # class variable
#     def __init__(self,name):
#         self.nm=name     # Instance variable
# e1=Employee("Pavan")
# e2=Employee("Kumar")
# print(e1.nm,e1.company)
# print(e2.nm,e2.company)


# Comstructor -- is a special method , automatically called when an object is created
# whi it is needed :
# To initialize the data
# Avoid the seperate setup methods
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("Pavan",21)
# p2=Person("Kumar",22)
# print(p1.name,p1.age)
# print(p2.name,p2.age)

# without constructor - Bad practice

# class Person():
#     def setData(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)

# p1=Person()
# p1.setData("Pavan")
# p1.display()


# Methods - Functions inside the class, they work on the data of the class/object
# types :
# 1.Instance Method
# 2.Class Method
# 3.Static Method


# Instance Method - Works with the object data
# It must use self as the first parameter
# self - self refers the current object and allows to access to instance variables

# class Student():
#     s="hi"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(self.name,self.marks,self.s)
# s1=Student("Pavan",100)
# s1.display()
        

# class method - works with class variables not with object variables
# uses  - @classmethod decorator
# Takes cls as first parameter
# class Employee():
#     company="Google"
#     @classmethod
#     def change_company(cls):
#         cls.company="Microsoft"
# print(Employee.company)
# Employee.change_company()
# print(Employee.company)


# static method - does not use self or cls
# works like a normal function
# kept inside a class for logical grouping
# uses @staticmethod decorator

# class Mathutils():
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Mathutils.add(5,4))


# Constructor - special method automatically called when an object is created
# __init__()
# types :
# 1.Default Constructor
# 2.Parameterized Constructor
# 3.Non Parameterized constructor

# constructor with only one parameter (self) - non parametrized constructor
# class Student():
#     def __init__(Self):
#         print("Constructor called")
# s1=Student()

# constructor with parameters - parameterized constructor
# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(self.name,self.marks)
# s1=Student("Pavan",85)
# s2=Student("Kumar",95)
# s1.display()
# s2.display()


# Default constructor - if no constructor is written , python creates one automatically.

# class Default_constructor():
#     def method(self):
#         print("I am in method")
# dc=Default_constructor()
# dc.method()


# Python does not support method overloading, so:
# Multiple constructors are not allowed

# class Test():
#     def __init__(self):
#         print("One")
#     def __init__(self):
#         print("Two")
# t=Test()

# for above only the last constructor works

# constructor in inheritance

# class Parent():
#     def __int__(self):
#         print("Parent Constructor")
# class Child(Parent):
#     def __init__(self):
#         print("Child Constructor")
# c=Child()

# Parent constructor not called

# we can call the parent's constructor in child class using super()

# class Parent():
#     def __init__(self):
#         print("Parent Constructor")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child Constructor")
# c=Child()

# constructor calling - calling one constructor from another.
class A():
    def __init__(self):
        print("Class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Class B")
class C(B):
    def __init__(self):
        super().__init__()
        print("Class C")
c=C()