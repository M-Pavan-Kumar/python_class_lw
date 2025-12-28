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
# class A():
#     def __init__(self):
#         print("Class A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Class B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Class C")
# c=C()


# Access Modifiers - controls who can access the variables and methods of a class.
# they help in data hiding, security, and encapsulation.

# Types: 
# 1.Public 
# 2.Protected
# Private

# 1.Public - accessible from anywhere
# class Student():
#     def __init__(self,name):
#         self.name=name   # public variable
#     def show(self): # public method
#         print(self.name)
# s=Student("Pavan")
# print(s.name)
# s.show()

# 2. Protected Access Modifier
# Accessed within the class and in its child classes

# class Parent():
#     def __init__(self):
#         self._money=5000  # Protected Varaible
# class Child(Parent):
#     def show(self):
#         print(self._money)
# child=Child()
# child.show()


# 3.Private access modifier
# accessible only inside the class
# class Bank():
#     def __init__(self):
#         self.__balance=10000  # Private Variable
#     def show_balance(self):
#         print(self.__balance) 
# b=Bank()
# b.show_balance()


# Private methods
# class Demo():
#     def __show(self):
#         print("Private method")
#     def access(self):
#         self.__show()
# d=Demo()
# d.access()

# Encapsulation - process of binding the data(variables) and methods(behaviors) into a single unit (class) and restricting the direct access to the data.
# Data hiding and controlled access

# encapsulation is achieved through the private varibles(__var)
# and using public methods (getters/setters)

# why encapsulation needed?
# protects the data from unathorized access
# improves the security
# makes the code maintainable
# controls how data is modified

# without encapsulation
# class Bank1():
#     balance=5000
# b1=Bank1()
# print(b1.balance)

# with encapsulation
# class Bank2():
#     def __init__(self):
#         self.__balance=3000  # private variables
# b2=Bank2()
# print(b2.__balance)   # error('Bank2' object has no attribute '__balance') 


# encapsulation with getter and setter methods
# class Bank():
#     def __init__(self):
#         self.__balance=5000
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#     def get_balance(self):
#         return self.__balance
# b=Bank()
# print(b.get_balance())
# b.deposit(500)
# print(b.get_balance())
# b.withdraw(4000)
# print(b.get_balance())


# class Student():
#     def __init__(self):
#         self.__marks=0
#     def set_marks(self,marks):
#         if(marks>self.__marks):
#             self.__marks=marks
#     def getMarks(self):
#         return self.__marks
# s=Student()
# print(s.getMarks())
# s.set_marks(500)
# print(s.getMarks())
# s.set_marks(600)
# print(s.getMarks())


# name Mangling - if you start a variable or method with two underscores (like __variable_name), pyhton automatically chnages its name behind the scenes .
# original name - __variable_name
# new mangled_name - _Classname__variable_name
# why needed ? - to prevent accidents during inheritance
# for examples if we have parent class and child class ,if both classes have common variables with same name ,
# name mangling ensures that they dont accidently overwrite each other.

# encapsulation with Protected variables
# class Account():
#     def __init__(self):
#         self._pin=1234
# class Atm(Account):
#     def show_pin(self):
#         print(self._pin)
# atm=Atm()
# atm.show_pin()


# login system example using encapsulation
# class Login():
#     def __init__(self,password):
#         self.__password=password
#     def check_password(self,pwd):
#         return self.__password==pwd
# l=Login("admin123")
# print(l.check_password("wrong"))
# print(l.check_password("admin123"))



# Abstraction
# -- process of hiding implementation details and showing only essential features to the user 
# in simple what to do is shown and how to do is hidden
#  why do we need abstraction ? 
# - Reduces the complexity
# - makes code flexible
# - allows independent implementation
# - improves the security

# Example : 
# atm - user sees withdraw,deposit
# internal logic - hidden
# user does not know how money is processed


# How abstraction is achieved ?
# - Abstract classes
# - Interfaces (via Abstract Base Classes - ABC)

# Abstract Class
# - Cannot be instantiated
# - contains abstract methods
# - Acts as a blueprint

# syntax
# from abc import ABC,abstractmethod
# class ClassName(ABC):
#     @abstractmethod
#     def method(self):
#         pass

# example
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car was started")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike was started")
# v=Vehicle() # TypeError: Can't instantiate abstract class Vehicle with abstract methods start
# c=Car()
# c.start()
# b=Bike()
# b.start()



# Note : 
# - we cannot create objects for abstract classes
# - Abstract classes can have normal methods too
# - child class can implement the abstract methods

# Abstract class with normal methods and abstract methods
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     def show(self):
#         print("Shape class")
#     @abstractmethod
#     def area(self):
#         pass
# class Square(Shape):
#     def area(self,side):
#         return self.side*self.side
# class Rectangle(Shape):
#     def area(self,l,b):
#         return self.l*self.b
# r=Rectangle()
# print(r.area(5,10))

# s=Square()
# print(s.area(5))


# Multiple abstarct methods 
# from abc import ABC,abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withdraw(self):
#         pass
# class MyBank(Bank):
#     def deposit(self):
#         print("Deposit done successfully")
#     def withdraw(self):
#         print("Amount withdrawn successfully")
# mybnk=MyBank()
# mybnk.deposit()
# mybnk.withdraw()

# Interface in python :
# - pyhton does not have a seperate interface like java.
# - But abstract classes with only abstract methods acts as interfaces

# Interface example :
# from abc import ABC,abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
# class Upi(Payment):
#     def pay(self,amount):
#         print("Paid ",amount," using UPI")
# class Card(Payment):
#     def pay(self,amount):
#         print("Paid ",amount," using Card")
# upi=Upi()
# upi.pay(5000)
# crd=Card()
# crd.pay(10000)

# # Abstract class + constructor
# from abc import ABC,abstractmethod
# class Device(ABC):
#     def __init__(self,brand):
#         self.brand=brand
#     @abstractmethod
#     def start(self):
#         pass
# class Laptop(Device):
#     def start(self):
#         print(self.brand, "laptop started")
# class PC(Device):
#     def start(self):
#         print(self.brand, "PC Started")
# l=Laptop("ASUS")
# l.start()
# pc=PC("DELL")
# pc.start()

# Abstraction vs Interface
# python does not have a seperate interface keyword in like java.
# interfaces in python are implemented using Abstract Base Classes (ABC)

# Interface :
# interface defines only method declarations(no logic) that a class must implement
# Achieved using - abstract classes with only contains abstract methods but not contain normal methods

# abstraction - partial implementation allowed (abstract methods + normal methods,can have constructor, can have variables)
# interface - no implementation at all (only abstract methods,no method implementation)

# Polymorphism :
# - one name , many forms
# - same method/function/operator behaves differently depends on :
#   -- object
#   -- Data type
#   -- context 

# why polymorphism?
# - improves flexibility
# - reduces the code duplication
# - makes the code extensible
# - suppports abstarction and inheritance

# Real world example :
# ATM -> withdraw
# - SBI ATM -> different logic
# - HDFC ATM -> different logic
# same action but different behaviour

# Types of polymorphism in pyhton
# 1.Run time polymorphism    -  Method overriding
# 2.Complile time polymorphism  - Method overloading
# 3.Operator overloading
# 4.Function polymorphism (Duck Typing)


# Compile time polymorphism - Method overloading --> class can have multiple methods with same name but with different parameters.To overload a method we must change the number of parameters or type of parameters or both
# - pyhton does not support method overloading like java, because pyhon is dynamically typed language 
# - Achieved using default arguments or varible length arguments(*args) or MultipleDispatch

# # using default arguments
# class claculator():
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
# c=claculator()
# print(c.add(2,3))
# print(c.add(1,2,3))

# # using *args
# class Demo():
#     def show(self,*args):
#         print(args)
# d=Demo()
# d.show(3)
# d.show(3,4,5)
# d.show(4,5,6)

# using MultipleDispatch
# from multipledispatch import dispatch
# class Example():
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         return a+b+c
# e=Example()
# print(e.add(5,10))
# print(e.add(2,3,4))


# Run time polymorphism - Method overriding --> defining a method in subclass with same name as method in super class, in this time python interpreter determines that which method to call at runtime based on the actual object being refered to.

# - happens at runtime
# - depends on object type

# Example
# class Parent():
#     def show(self):
#         print("I am parent method")
# class Child(Parent):
#     def show(self):
#         print("I am child method")
# obj=Child()
# obj.show()

# using super()
# class Parent():
#     def show(self):
#         print("I am parent method")
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("I am child method")
# obj=Child()
# obj.show()