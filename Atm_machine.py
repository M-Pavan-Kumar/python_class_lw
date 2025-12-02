amount=int(input("enter amount to withdraw : "))
if amount%100==0:
    if amount>=500:
        f=amount//500
        print("500 notes --",f)
        amount=amount%500   # amount=amount-f*500
    if amount>=200:
        t=amount//200
        print("200 notes -- ",t)
        amount=amount%200
    if amount>=100:
        h=amount//100
        print("100 notes -- ",h)
        # amount=amount%100

else:
    print("invalid input")