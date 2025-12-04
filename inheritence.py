# Inheritance
# parent class:gives properties
# child class:takes properties

# syntax
# class Parent_class:
#     stmnts
# class Child_class(Parent_class):
#     stmnts

# class A:
#     pass
# class B(A):
#     pass

# super() 
# -> use with variable 
# -> use with method
# -> use with constructor

# class Movie:
#     name="chotu"
#     def display(self):
#         print("Movie Information :")
#     def show(self):
#         print("Budget: 100cr")
# print()
# class Director(Movie):
#     def movie_info2(self,name,year,actor):
#         print("Movie: ",super().name)
#         print("Year: ",year)
#         print("Actor: ",actor)
#     def budget(self):
#         super().display()
#         super().show()
# # ob_p=Movie()
# ob_c=Director()
# # ob_p.movie_info("OG",2025,"pk")
# ob_c.budget()
# ob_c.movie_info2("sahoo",2013,"Prabhas")


# class Movie:
#     name="abcd"
#     year=2022
#     actor="chotu"
#     def display(self):
#         print("Movie Information :")
#     def show(self):
#         print("Budget: 100cr")
# print()
# class Director(Movie):
#     def movie_info2(self,name,year,actor):
#         print("**Accessing variables from parent with super()**")
#         print("Movie: ",super().name)
#         print("Year: ",super().year)
#         print("Actor: ",super().actor)
#         print("**Accessing variables without super()**")
#         print("Movie: ",name)
#         print("Year: ",year)
#         print("Actor: ",actor)
#     def budget(self):
#         super().display()
#         super().show()

# ob_c=Director()
# ob_c.budget()
# ob_c.movie_info2("sahoo",2013,"Prabhas")

# super with variables
# class A:
#     age=21
    
# class B(A):
#     age=22
#     def show(self):
#         print(self.age)
#         print(super().age)

# obj=B()
# obj.show()

# # super with method
# class A:
#     def addition(self):
#         print("Sum: ",20+30)
# class B(A):
#     def subraction(self):
#         super().addition()
#         print("Subraction: ",30-10)
# obj=B()
# obj.subraction()


# super() with constructor
# class A:
#     def __init__(self):
#         print("I am parent class constructor")
# class B(A):
#     def __init__(self):
#         print("I am child class constructor")
#         super().__init__()
# obj=B()


# single inheritance
# class A:
#     def display(self):
#         print("I am parent method")
# class B(A):
#     def display(self):
#         print("I am a child class ")
#         super().display()
# obj=B()
# obj.display()

# multilevel inheritance
# class A:
#     def display(self):
#         print("I am Grand parent method")
# class B(A):
#     def display(self):
#         print("I am a parent  method ")
#         super().display()
# class C(B):
#     def display(self):
#         print("I am a child class method")
#         super().display()
# obj=C()
# obj.display()

# multiple inheritance
# class A:
#     def display1(self):
#         print("I am Grand parent1 method")
# class B:
#     def display2(self):
#         print("I am Grand parent2 method")
# class C(A,B):
#     def display(self):
#         print("I am a child class method")
#         super().display1()
#         super().display2()
# obj=C()
# obj.display()

# Multiple inheritance


