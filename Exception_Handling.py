# try:
#     # print(2/0)
#     n1=int(input("Enter a value : "))
#     n2=int(input("Enter  a value : "))
#     # print(n1+n2)
#     # print(m)

    
# except ZeroDivisionError:
#     print("Zero division Error occured")
# except NameError:
#     print("Name error occured")
# except TypeError:
#     print("Type error occured")
# except ValueError:
#     print("value Error occured")
# except:
#     print("This is final except")
# finally:
#     print("Final block")


# lst=[5,6,0,10,5]
# for req in lst:
#     try:
#         n=10000
#         res=n/req
#         print("Processed successfully : ",res)
#     except ZeroDivisionError:
#         print("Zero Division error occured")
#     else:
#         print("This is else")


# try:
#     a=int(input())
#     b=int(input())
#     p=a*b
#     print(p)
# except NameError:
#     print("Name Error occured ")
# except TypeError:
#     print("Type error occured")
# except ValueError:
#     print("value Error occured")
# except:
#     print("This is final except")
# else:
#     print("This is else block ")
# finally:
#     print("This is the final block")


# Calculator app

# print("--- Calculator app ---")
# print("Choose your choice +,-,*,/ or q (to quit)")
# while True:
#     try:
#         choice=input("Enter your choice: ")
#         if choice.lower()=="q":
#             print("Thanks for using!")
#             break
        
#         if choice in ["+","-","*","/"]:
#             n1=int(input("Enter A number : "))
#             n2=int(input("Enter A number : "))
#             if choice=="+":
#                 print(f"{n1}+{n2}= {n1+n2}")
#             elif choice=="-":
#                 print(f"{n1}-{n2}= {n1-n2}")
#             elif choice=="*":
#                 print(f"{n1}*{n2}= {n1*n2}")
#             elif choice=="/":
#                 try:
#                     print(f"{n1}/{n2}= {n1/n2}")
#                 except ZeroDivisionError:
#                     print("Zero Division Error occured")
                
#         else:
#             print("Inavid Choice, Try again")
#     except NameError:
#         print("Name Error occured ")
#     except TypeError:
#         print("Type error occured")
#     except ValueError:
#         print("value Error occured")    
#     except:
#         print("Error occured")

try:
    n=int(input("Enter a number : "))
    if n<0:
        raise ValueError("This is value error")
except Exception as e:
    print(e)
print("Code ended successfully")
    
