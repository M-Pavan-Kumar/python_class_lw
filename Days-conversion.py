dys=int(input())
yrs=dys//365
dys=dys%365
mnths=dys//30
dys=mnths%30
print(yrs,mnths,dys)