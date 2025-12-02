

'''
# Gcd or HCF 
n1=int(input("Enter number: "))
n2=int(input("Enter number: "))

while n2!=0:
    temp=n2
    n2=n1%n2
    n1=temp
print("GCD is : ",n1)


'''


'''
# Lcm of two numbers
# n1=int(input("Enter number: "))
# n2=int(input("Enter number: "))
# a,b=n1,n2
# while n2!=0:
#     temp=n2
#     n2=n1%n2
#     n1=temp
# gcd=n1
# lcm=(a*b)//gcd
# print("Lcm is : ",lcm)


#  or 

# n1=int(input("Enter number: "))
# n2=int(input("Enter number: "))
# greater=n1 if n1>n1 else n2
# while True:
#     if greater %n1==0 and greater %n2 ==0:
#         print("LCM is :",greater)
#         break
#     greater+=1

'''


'''
# Polindrome number check
n=int(input("Enter a number :"))
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if n==rev:
    print("Polindrome Number")
else:
    print("Not a polindrome number")

'''


'''
# Armstrong number check

n=int(input("Enter a number :"))
temp1=temp2=n
count=0
while temp1>0:
    count+=1
    temp1//=10
sum=0
while temp2>0:
    digit=temp2%10
    sum+=digit**count
    temp2//=10
if sum==n:
    print("Armstrong number")
else:
    print("Not a Armstrong number")

'''

'''
# Armstrong numbers in a given range
start=int(input("Enter Start value : "))
end=int(input("Enter end value : "))
for n in range(start,end+1):
    temp1=temp2=n
    count=0
    while temp1>0:
        count+=1
        temp1//=10
    sum=0
    while temp2>0:
        digit=temp2%10
        sum+=digit**count
        temp2//=10
    if sum==n:
       print(n,end=" ")
'''

'''
# Harshad number (Niven number)
n=int(input("Enter a number : "))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp//=10
if n%sum==0:
    print("Harshad numeber")
else:
    print("Not a harshad number")

'''

'''
# Neon number

n=int(input("Enter a number : "))
square=n*n
sum=0
while square>0:
    digit=square%10
    sum=sum+digit
    square//=10
if sum==n:
    print("Neon number")
else:
    print("Not a Neon number")

'''

# Happy number
n=int(input("Enter a number : "))
temp=n
seen=set()
is_happy=False

while temp!=1 and temp not in seen:
    seen.add(temp)
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**2
        temp//=10
    temp=sum
if sum==1:
    print("Happy number")
else:
    print("Not a happy number")
    



'''
# Magic Number

# A number is Magic if the repeated sum of its digits equals 1.
# Example → 19 → 1 + 9 = 10 → 1 + 0 = 1

n =int(input("Enter a number : "))
temp=n
while temp>9:
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit
        temp//=10
    temp=sum
if temp==1:
    print("Magic number")
else:
    print("Not a magic number")
    
'''

'''
# Automorphic number or not

n=int(input("Enter a number : "))
square=n*n
c=0
temp=n
while temp>0:
    c+=1
    temp//=10
i=1
pow=1
while i<=c:
    pow=pow*10
    i+=1
if square%pow==n:
    print("Automorpic number")
else:
    print("Not a Automorphic number")


'''
'''
# Friendly pair or not
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
sum1=0
i=1
while i<=a:
    if a%i==0:
        sum1+=i
    i+=1
sum2=0
j=1
while j<=b:
    if b%j==0:
        sum2+=j
    j+=1
if sum1*b==sum2*a:
    print("Friendly pair")
else:
    print("Not a friendly pair")

'''
'''
# Amicable pair or not 
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
sum1=0
i=1
while i<a:
    if a%i==0:
        sum1+=i
    i+=1
sum2=0
j=1
while j<b:
    if b%j==0:
        sum2+=j
    j+=1
if sum1==b and sum2==a:
    print("Amicable pair")
else:
    print("Not an Amicable pair")

    
'''

'''

# Check given number is prime or not 
n=int(input("Enter a number : "))
is_prime=True
if n==0 or n==1:
    print(f"{n} is not a prime number")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
if(is_prime):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

'''

'''

# Prime number in a given range
start=int(input("Enter start value : "))
end=int(input("Enter end value : "))
for i in range(start,end+1):
    is_prime=True
    if i==0 or i==1:
        is_prime=False
    elif i>1:
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
    if(is_prime):
        print(i,end=" ")

'''