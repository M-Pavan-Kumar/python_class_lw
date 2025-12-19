# ABC - Abstarct Base Class

# from abc import ABC,abstractmethod
# class Student(ABC):
#     @abstractmethod
#     def display(self):
#         pass
# class Cse_students(Student):
#     def display(self):
#         print("All cse students data")
# obj=Cse_students()
# # obj1=Student()  # we cannot create objects for abstract class
# obj.display()


# from abc import ABC , abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         print(self.side*self.side)
# class Triangle(Shape):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area(self):
#         print(0.5*self.b*self.h)

# square=Square(5)
# square.area()
# triangle=Triangle(3,2)
# triangle.area()


import random
from abc import ABC,abstractmethod

class Recharge(ABC):
    @abstractmethod
    def display(self):
        pass
class Phonepe(Recharge):
    def __init__(self,amount):
        self.amount=amount
    def display(self):
        print("Recharge succesful throuh Phonepe, Amount is : ",self.amount)
        print("You got 10 % discount , Discount is : ",self.amount*0.1)
class Googlepay(Recharge):
    def __init__(self,amount):
        self.amount=amount
    def display(self):
        print("Recharge successful through Google pay, Amount is : ",self.amount)
        cashback=random.randint(1,10)
        print("You got cashback, Cashback is : ",cashback)
        print("Amount to paid is : ",self.amount-cashback)

phonepe=Phonepe(350)
phonepe.display()
googlepay=Googlepay(360)
googlepay.display()


