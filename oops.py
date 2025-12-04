# Example 1
# class Director:
#     def display(self):
#         print("**** Details of director ***")
#         print("Abc")
#         print("Def")
#         print("21")
# obj=Director()
# obj.display()
# obj.display()w

# Example 2
# class Director:
#     name="abc"     # class variables
#     movie="def"
#     age=50
#     def display(self):
#         print("**** Details of director ***")
#         print("Name: ",self.name)
#         print("Movie: ",self.movie)
#         print("Age: ",self.age)
# obj=Director()
# obj.display()
# obj.display()
# print(Director.name)
# print(Director.movie)
# print(Director.display())  # this gives error we cannot access the methods using class

# Example 3
# class Director:
#     name="abc"     # class variables
#     movie="def"
#     age=50
#     def display(self):
#         print("**** Details of director ***")
#         print("Name: ",self.name)
#         print("Movie: ",self.movie)
#         print("Age: ",self.age)
# obj=Director()
# obj.name="pavan"
# obj.movie="xyz"
# obj.age=21
# obj.display()
# obj.display()


# Example 4
# class Director:
#     name="abc"     # class variables
#     movie="def"
#     age=50
#     def display(self,name,movie,age):
#         print("**** Details of director ***")
#         print("Name: ",name)
#         print("Movie: ",movie)
#         print("Age: ",age)
# obj=Director()
# obj.name="pavan"
# obj.movie="xyz"
# obj.age=21
# obj.display(obj.name,obj.movie,obj.age)
# obj.display("chotu","bigboss",25)


# Automatically called when an object is created.
# Used to initialize variables
# First method to be executed in a program is constructor

# class Movie:
#     def __init__(self): # constructor without parameters
#         print("Movie information")
#     def movie_info(self,name,year,actor):
#         print("Movie name  :",name)
#         print("year: ",year)
#         print("Actor: ",actor)
# obj=Movie()
# obj.movie_info("Eeega",2013,"Nani")

class Movie:
    def __init__(self,name,year,actor): # constructor with parameters
        self.n=name
        self.y=year
        self.a=actor
    def movie_info(self):
        print("Movie name  :",self.n)
        print("year: ",self.y)
        print("Actor: ",self.a)
obj=Movie("Eeega",2013,"Nani")
obj.movie_info()
print()
class Movie:
    def __init__(self): # default constructor
        self.n="OG"
        self.y=2025
        self.a="PK"
    def movie_info(self):
        print("Movie name  :",self.n)
        print("year: ",self.y)
        print("Actor: ",self.a)
obj=Movie()
obj.movie_info()
