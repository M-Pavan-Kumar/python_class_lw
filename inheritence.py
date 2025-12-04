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