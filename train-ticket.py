import sys
print("*** Sabari Express ***")
print("1. Sleeper - 450")
print("2. One Tier Ac - 800 ")
print("3. Two Tier Ac - 1000")
print("4. Three Tier Ac - 1300")
print("5 .Exit")
ticket_count=int(input("enter number of tickets : "))
cost=0
discount=0
if ticket_count>6:
    print("Not allowed to book more than 6 tickets")
    # sys.exit(0)
else:
    choice=int(input("Enter type of seat from the list : "))    
    if choice==1:
        cost=450*ticket_count
    elif choice==2:
        cost=800*ticket_count
    elif choice==3 :
        cost=1000*ticket_count
    elif choice==4:
        cost=1300*ticket_count
    elif choice==5:
        print("Exit program")
    else:
        print("Inavalid choice")
    if cost>1000:
        discount=50
        cost=cost-discount
    if cost>0:
        gst=cost*0.05
        ic=cost*0.02
        finalcost=cost+gst+ic
        print("Tickets cost : ",cost)
        print("Gst : ",gst)
        print("Internet costs : ",ic)
        print("Discount : ",discount)
        print("Final Amount : ",finalcost)