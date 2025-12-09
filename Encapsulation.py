# # public
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s=Student("Ram",21)
# print(s.name,s.age)

# # protected
# class Company:
#     def __init__(self,name,age,salary):
#         self._name=name
#         self._age=age
#         self._salary=salary
# class Employee(Company):
#         def display(self):
#              print("Salary: ",self._salary)
# e=Employee("pavan",21,80000)
# e.display()

# getter and setter methods


class Bank:
    def __init__(self):
        self.__balance=60000
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Amount Deposited successfully.")
        else:
            print("Amount not deposited")
    def get_balance(self):
        return self.__balance
b=Bank()
print("Old balance: ",b.get_balance())
b.set_balance(20000)
print("New balance : ",b.get_balance())




    
    