# types of arguments
# 1.Positional
# 2.Keyword
# 3.default
# 4.variable length aguments
# 5.varibale length keyword argumnets

# positional arguments
# def student_details(name,rollno,marks):
#     print("Name: ",name)
#     print("Roll number : ",rollno)
#     print("Marks :",marks)
# student_details("Pavan",123,95.0)
# print()


# # keyword arguments
# def student_details(name,rollno,marks):
#     print("Name: ",name)
#     print("Roll number : ",rollno)
#     print("Marks :",marks)
# student_details(marks=95.0,name="Pavan",rollno=123)
# print()

# # default argumnets
# def student_details(name="kumar",rollno=111,marks=0):
#     print("Name: ",name)
#     print("Roll number : ",rollno)
#     print("Marks :",marks)

# student_details()
# print()
# student_details(95.0)
# print()
# student_details(95.0,"Pavan")
# print()
# student_details(95.0,"Pavan",123)
# print()


# # variable length arguments
# def student_details(*details):
#     print("Details :",details)

# student_details("chotu")
# student_details("pavan",21,300,"cse")
# student_details("kumar",22,500,"AI ML")
# student_details("hi","hello","how are you?")
# print()

# # variable length keyword argumnts
# def student_details(**details):
#     print("Details :",details)

# student_details(name="chotu")
# student_details(name="pavan",age=21,marks=300,branch="cse")
# student_details(name="kumar",age=22,marks=500,branch="AI ML")

# function return statemnt  --- fruitful function
# function without return --- void functions
# def student_info(name,rollno):
#     return name,rollno
# data=student_info("pavan",3363)
# print(data)

# def marks_info(marks):
#     return sum(marks)//len(marks)
# marks=list(map(int,input("Enter 5 subject marks : ").split()))
# avg=marks_info(marks)
# print(avg)



# Banking Application
# def deposit(bal,amt):
#     if amt>0 and amt<=50000:
#         bal+=amt
#         print("Amount Deposited successfully ")
#     else:
#         print("Invalid amount")
# def withdraw(bal,amt):
#     if amt>0 and amt<=10000:
#         if amt<=bal:
#             bal-=amt
#             print("Amount Withdrawn successfully ")
#         else:
#             print("Insufficient balance")
#     else:
#         print("Invalid amount")
# def getbalance(bal):
#     return bal
# # bal=5000
# def menu():
#     bal=5000
#     print("***BANK MENU***")
#     print("1.Deposit")
#     print("2.Withdraw")
#     print("3.Balance Check")
#     print("4.Exit")
#     choice=int(input("Choose your option : "))
#     if choice==1:
#         amt=int(input("Enter amount to deposit: "))
#         deposit(bal,amt)
       
#     elif choice==2:
#         amt=int(input("Enter amount to withdraw: "))
#         withdraw(bal,amt)
        
#     elif choice==3:
#         print("Available balance is : ",getbalance(bal))
#     elif choice==4:
#         print("Thanks for using our bank application")
#         return
#     else:
#         print("Invalid choice try again")
# menu()

# Student Records Maintainence System using functions



# def add_student(records,rollno,name,percentage):
#     records[rollno]={"name":name,"percentage":percentage}
#     print("Record added successfully")
#     return records

# def remove_student(records,roll_no):
#     if roll_no in records:
#         del records[roll_no]
#     else:
#         print("Roll number not found")
#     return records

# def show_all(records):
#     if not records:
#         print("No records available")
#         return
#     print("______________________________________")
#     print("{:<10} {:<20} {:<10}".format("rollno","name","percentage"))
#     print("______________________________________")
#     for roll_no,info in records.items():
#         print("{:<10} {:<20} {:<10}".format(roll_no,info["name"],info["percentage"]))
#     print("______________________________________")

# def main():
#     records={}
#     while True:
#         print("___ student Menu ___")
#         print("1. Add student")
#         print("2. Remove student")
#         print("3. View all students")
#         print("4. Exit")
#         choice=int(input("Enter Your choice : "))
#         if choice==1:
#             roll_no=int(input("enter roll number: "))
#             name=input("Enter Name : ")
#             percentage=float(input("Enter Percentage : "))
#             records=add_student(records,roll_no,name,percentage)
#         elif choice==2:
#             roll_no=int(input("enter roll number: "))
#             records=remove_student(records,roll_no)
#         elif choice==3:
#             show_all(records)
#         elif choice==4:
#             print("Existed successfully")
#             break
#         else:
#             print("Invalid choice")

# main()


# Scope of a variable
# local scope
# global scope
# b=1000
# def display():
#     a=100
#     print("A value is  : ",a)
#     print("B value is  (inside the function) : ",b)


# display()
# print("B value is (outside the function) : ",b)

 
# b=1000
# def display():
#     global b
#     b=10
#     print("B value : ",b)
# display()
# print("B value is : ",b)


# recursion
# base condition -- when the function is going to stop
# recursive condition -- calls your function recursively



# sum of two numbers using recusion
# a=10
# b=5
# def add(a,b):
#     if b==0:
#         return a
#     return add(a+1,b-1)
# addition=add(a,b)
# print(addition)

# subraction of two numbers using recursion
# a=10
# b=5
# def sub(a,b):
#     if b==0:
#         return a
#     return sub(a-1,b-1)
# print(sub(a,b))

# sum of n natural numbers using recursion
# n=int(input("Enter number of elements : "))
# def add(n):
#     if n==0:
#         return 0
#     return n+add(n-1)
# print(add(n))

# sum of digits in a number using recursion
# n=123
# def add_digit(n):
#     if n==0:
#         return 0
#     return n%10+add_digit(n//10)
# print(add_digit(n))
    
# reverse of a given number using recursion
n=int(input("Enter a number: "))
def reverse(n,rev=0):
    if n==0:
        return rev
    digit=n%10
    n=n//10
    rev=rev*10+digit
    return reverse(n,rev)
print(reverse(n))
