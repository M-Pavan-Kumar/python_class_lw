
"""
# Odd numbers sum and even numbers sum

n=int(input("Enter n value: "))
o_sum=0
e_sum=0
i=1
while i<=n:
    if i%2==0:
        e_sum+=i
    else:
        o_sum+=i
    i=i+1
print("Even sum : ",e_sum)
print("Odd sum : ",o_sum)

"""

""""
# sum of multiples of 5 and 7
n=int(input("Enter n value: "))
sum=0
i=1
while i<=n:
    if i%5==0 or i%7==0:
        # print(i)
        sum=sum+i
    i=i+1
print("sum is : ",sum)


# Tracing 
# Loop 1
#  sum=0,n=10,i=1
# while 1<=10: True
    if 1%5==0 or 1%7==0: False
        skip
    i=i+1=i+1=2

"""
'''
n=int(input("enter numbers: "))
sum=0
while n>0:
    if n%3!=0 and n%11!=0:
        # print(n)
        sum+=n
    n=n-1
print("Sum is : ",sum)

'''
'''
# Adding two numbers until users stops
choice=input("Enter choice Y or N: ")
while choice=="y" or choice=="Y":
    n1=int(input("enter first number: "))
    n2=int(input("enter second number: "))
    print("Sum : ",n1+n2)
    choice=input("do you want to repeat again y or n :")

'''
'''
print("***Canteen Menu***")
print("1.Idly-30 \n2.Dosa-40 \n3.Poori-40 \n4.Bonda-30")
bill=0
choice=input("enter order please (y or no) :")
while choice=="y" or choice=="Y":
    option=int(input("Choose the item :"))
    q=int(input("How many plates :"))
    if option==1:
        cost=q*30
    elif option==2:
        cost=q*40
    elif option==3:
        cost=q*40
    elif option==4:
        cost=q*30
    else:
        print("Invalid choice")
    choice=input("Do you want to order something: ")
    bill=bill+cost
print("Your bill is : ",bill)
     
'''


'''
print("*** Electricity Bill ***")
print("1.100  - 2rs")
print("2.200  - 3rs")
print("3.300  - 4rs")
print("4.>300 - 7rs")

i=1
total_bill=0
ch=input("Want to pay Electricity bill : ")
while ch=="y" or ch=="Y":
    units=int(input("Enter consumed units : "))
    if units>0 and units<=100:
        bill=units*2
    elif units>100 and units <=200:
        bill=100*2+(units-100)*3
    elif units>200 and units<=300:
        bill=100*2+100*3+(units-200)
    else:
        bill=100*2+100*3+100*4+(units-300)*7
    print("Customer ",i,"bill is :",bill)
    i=i+1
    total_bill=total_bill+bill
    ch=input("do you want to pay another electricity bill :  ")
print("Todays collection : ",total_bill)


'''

'''
n=1234

(n//100)%10


'''

'''
# Counting the number of digits in a number
n=int(input("Enter number : "))
c=0
while n>0:
    n=n//10
    c+=1
print("Number of digits : ",c)

'''
'''
# differene of combination of even and odd numbers 

n=int(input("Enter number : "))
n1=0
n2=0
p1=1
p2=1
while n>0:
    digit=n%10
    if(digit%2==0):
        n1=n1+p1*digit
        p1=p1*10
    else:
        n2=n2+p2*digit
        p2=p2*10
    n=n//10
# print(n1,n2)
print("Difference is : ",n1-n2)

'''






'''

# Strong number

# 145 ==> 1!+4!+5!=1+24+120=145


n=int(input("Enter a number: "))
temp=n
sum=0
while temp>0:
    digit=temp%10
    f=1
    while digit>0:
        f=f*digit
        digit=digit-1
    sum=sum+f
    temp=temp//10
# print("Strong number" if sum==n else "Not strong number")
print("Strong number") if sum==n else print("Not strong")

'''


# Perfect number

# 6 ---> 1,2,3 ---> 1+2+3=6 (sum of divisors excluding itself)



n=int(input("enter a number : "))
max=0
min=9
while n>0:
    digit=n%10
    if digit>max:
        max=digit 
    elif digit<min:
        min=digit
    n=n//10
print("Sum is : ",max+min)


    