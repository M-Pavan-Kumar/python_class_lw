# Example 1
# class Director:
#     def display(self):
#         print("**** Details of director ***")
#         print("Abc")
#         print("Def")
#         print("21")
# obj=Director()
# obj.display()
# obj.display()

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
class Director:
    name="abc"     # class variables
    movie="def"
    age=50
    def display(self,name,movie,age):
        print("**** Details of director ***")
        print("Name: ",name)
        print("Movie: ",movie)
        print("Age: ",age)
obj=Director()
obj.name="pavan"
obj.movie="xyz"
obj.age=21
obj.display(obj.name,obj.movie,obj.age)
obj.display("chotu","bigboss",25)
