try:
    # print(2/0)
    n1=int(input("Enter a value : "))
    n2=int(input("Enter  a value : "))
    # print(n1+n2)
    print(m)

    
except ZeroDivisionError:
    print("Zero division Error occured")
except NameError:
    print("Name error occured")
except TypeError:
    print("Type error occured")
except ValueError:
    print("value Error occured")
except:
    print("This is final except")
finally:
    print("Final block")