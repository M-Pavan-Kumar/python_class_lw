'''

#  for iteration_var in <sequence>:
    # statements



# for with range function

# range with one parameter
for i in range(10):
    print(i,end=" ")
print()

# range with two parameters
for i in range(4,10):
    print(i,end=" ")
print()

# range with three parameters
for i in range(1,10,3):
    print(i,end=" ")
print()

#  range in reverse order
for i in range(10,0,-1):
    print(i,end=" ")
print()


# for with list
for i in [1,2,3,4,5,6,7,5,8]:
    print(i,end=" ")
print()

# for with string

for i in "Prabhas":
    print(i,end=" - ")
print()




'''


'''
# n=int(input("Enter number: "))
# for i in range(n,0,-1):
#     if i%2==0:
#         print(i,end=" ")
# print()

# n=int(input("Enter number: "))
# for i in range(n,0,-2):
#     print(i,end=" ")
# print()

# Perfect number
# using for loop 
n=int(input("Enter number : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("Perfect number ")
else:
    print("Not a perfect number")


# using while
temp=n-1
sum=0
while temp>0:
    if n%temp==0:
        sum=sum+temp
    temp=temp-1
if sum==n:
    print("Perfect")
else:
    print("Not a perfect")



#  Perfect numbers in a given range  6,28,496,8128 .....

start=int(input("Enter start Value : "))
end=int(input("Enter End value : "))
for i in range(start,end+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if(sum==i):
        print(i,end=" ")


'''

'''
# Disarium number
num=int(input("Enter number : "))
count=0
temp1=temp2=num
while temp1>0:
    temp1=temp1//10
    count+=1
sum=0
while temp2>0:
     digit=temp2%10
     sum=sum+digit**count
     temp2//=10
     count-=1
if(sum==num):
     print("Disarium number")
else:
     print("Not a Disarium number")



# Disarium number in a given range

start=int(input("Enter start value : "))
end=int(input("Enter end value : "))
for i in range(start,end+1):
    count=0
    c=0
    temp1=temp2=i
    while temp1>0:
        temp1=temp1//10
        count+=1
    sum=0
    while temp2>0:
        digit=temp2%10
        sum=sum+digit**count
        temp2//=10
        count-=1
    if(sum==i):
        print(i,end=" ")

# Nth disarium number
start=int(input("Enter start value : "))
end=int(input("Enter end value : "))
pos=int(input("Enter Position : "))
dcount=0
for i in range(start,end+1):
    count=0
    temp1=temp2=i
    while temp1>0:
        temp1=temp1//10
        count+=1
    sum=0
    while temp2>0:
        digit=temp2%10
        sum=sum+digit**count
        temp2//=10
        count-=1

    if(sum==i):
        # print(i,end=" ")
        dcount+=1
        if dcount==pos:
            print(i)

'''

    


