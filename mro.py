# class A:
#     def show(self):
#         print("A")
# class B:
#     def show(self):
#         print("B")
# class C(A,B):
#     pass
# obj=C()
# obj.show()
# print(C.mro())

# isinstance() and issubclass()

class Animal:
    pass
class Dog(Animal):
    pass
d=Dog()
print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(isinstance(d,object))

print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))
print(issubclass(Dog,object))



