print("*** Hot pot Restaurant ***")
print("1.veg biryani - 200")
print("2.Paneer biryani - 250")
print("3.Mushroom biryani - 250")
print("4.Kaju biryani - 300")
print("5.Exit")
amount=0
item=int(input("Enter item number from menu : "))
if item==1:
    qntty=int(input("Enter number of parcels: "))
    amount=200*qntty
elif item==2:
    qntty=int(input("Enter number of parcels: "))
    amount=250*qntty
elif item==3:
    qntty=int(input("Enter number of parcels: "))
    amount=250*qntty
elif item==4:
    qntty=int(input("Enter number of parcels: "))
    amount=300*qntty
elif item==5:
    print("Thank you , Bye bye")
else:
    print("Inavalid choice")
if amount>=100:
    amount=amount*0.9
elif amount>=200:
    amount=amount*0.75

if amount>0:
    gst=amount*0.05
    st=amount*0.02
    tip=int(input("Enter tip amount : "))
    finalamount=amount+gst+st+tip
    print("Items cost : ",amount)
    print("GST : ",gst)
    print("Service Tax : ",st)
    print("Tip : ",tip)
    print("Final Bill : ",finalamount)
