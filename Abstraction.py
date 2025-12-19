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


# import random
# from abc import ABC,abstractmethod

# class Recharge(ABC):
#     @abstractmethod
#     def display(self):
#         pass
# class Phonepe(Recharge):
#     def __init__(self,amount):
#         self.amount=amount
#     def display(self):
#         print("Recharge succesful throuh Phonepe, Amount is : ",self.amount)
#         print("You got 10 % discount , Discount is : ",self.amount*0.1)
# class Googlepay(Recharge):
#     def __init__(self,amount):
#         self.amount=amount
#     def display(self):
#         print("Recharge successful through Google pay, Amount is : ",self.amount)
#         cashback=random.randint(1,10)
#         print("You got cashback, Cashback is : ",cashback)
#         print("Amount to paid is : ",self.amount-cashback)

# phonepe=Phonepe(350)
# phonepe.display()
# googlepay=Googlepay(360)
# googlepay.display()

import random
from abc import ABC,abstractmethod

class Recharge(ABC):
    @abstractmethod
    def display(self):
        pass
class Airtel(Recharge):
    def __init__(self,amount):
        self.amount=amount
    def display(self):
        print("Recharge succesful , Amount is : ",self.amount)
        discount=self.amount*0.1
        print("You got 10 % discount , Discount is : ",discount)
        total_amount=self.amount-discount
        print("Total amount  paid was: ",total_amount)
class Jio(Recharge):
    def __init__(self,amount):
        self.amount=amount
    def display(self):
        print("Recharge successful, Amount is : ",self.amount)
        cashback=random.randint(1,10)
        print("You got cashback, Cashback is : ",cashback)
        print("Amount  paid was : ",self.amount-cashback)



print("*** Select Provider ****")
print("1.Airtel")
print("2.Jio")
choice=input("Enter your choice 1 or 2 : ")
if choice=="1":
    print("*** Select Plan ***")
    print("1.500")
    print("2.350")
    plan=input("Enter Plan 1 or 2 : ")
    if plan=="1":
        airtel=Airtel(500)
        airtel.display()
    elif plan=="2":
        airtel=Airtel(350)
        airtel.display()
    else:
        print("Invalid Plan")
elif choice=="2":
    print("*** Select Plan ***")
    print("1.500")
    print("2.350")
    plan=input("Enter Plan 1 or 2 : ")
    if plan=="1":
        jio=Jio(500)
        jio.display()
    elif plan=="2":
        jio=Jio(350)
        jio.display()
    else:
        print("Invalid Plan")
else:
    print("Invalid Choice")


