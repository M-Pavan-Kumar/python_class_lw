# class A():
#     v1=2
#     v2=3
#     def method(self):
#         print("Hi, iam first method")

# print(A().v1)
# print(A().v2)
# A().method()

# p=A()              
# print(p.v1)
# print(p.v2)
# p.method()

# p1=A()
# p2=A()
# p1.v1=100
# print(p1.v1)
# print(p2.v1)


# class P():
#     def first(self):
#         print("This is first method")
# h=P()
# h.first()

# class Operation():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def ope(self):
#         return self.a+self.b
#     def display(self):
#        res= self.ope()
#        print(res)
# a=int(input("Enter A value: "))
# b=int(input("Enter B value: "))
# obj=Operation(a,b)
# obj.display()

# class Operation():
#     def __init__(self):
#         self.a=int(input("Enter A value: "))
#         self.b=int(input("Enter B value: "))
#     def ope(self):
#         return self.a+self.b
#     def display(self):
#        res= self.ope()
#        print(res)
# obj=Operation()
# obj.display()

# class Operation():
#     def __init__(self,a,b):
#         self.a=int(input("Enter A value: "))
#         self.b=int(input("Enter B value: "))
#     def ope(self):
#         return self.a+self.b
#     def display(self):
#        res= self.ope()
#        print(res)
# obj=Operation(a=10,b=20)
# obj.display()

# single inheritance
# class A():
#     def parent(self):
#         print("I parent class")
# class B(A):
#     def child(self):
#         print("I am child class")
# obj=B()
# obj.child()
# obj.parent()

# multilevel inheritance
# class A():
#     def first(self):
#         print("I am first method")
# class B(A):
#     def second(self):
#         print("I am second method")
# class C(B):
#     def third(self):
#         print("I am third method")        
# c_obj=C()
# b_obj=B()
# c_obj.first()
# c_obj.second()
# c_obj.third()


# Heirarchical inheritance
# class A():
#     def first(self):
#         print("I am first method")
# class B(A):
#     def second(self):
#         print("I am second method")
# class C(A):
#     def third(self):
#         print("I am third method")        
# c_obj=C()
# b_obj=B()
# c_obj.first()
# c_obj.third()
# b_obj.first()
# b_obj.second()

# Hybrid inheritance
class A():
    def first(self):
        print("I am first method")
class B(A):
    def second(self):
        print("I am second method")
class C(A,B):
    def third(self):
        print("I am third method")        
c_obj=C()
b_obj=B()
c_obj.first()
c_obj.second()
c_obj.third
c_obj.third()
