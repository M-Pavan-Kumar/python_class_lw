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


try:
    a=int(input())
    b=int(input())
    p=a*b
    print(p)
except NameError:
    print("Name Error occured ")
except TypeError:
    print("Type error occured")
except ValueError:
    print("value Error occured")
except:
    print("This is final except")
else:
    print("This is else block ")

    
