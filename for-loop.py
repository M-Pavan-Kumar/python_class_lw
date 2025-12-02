# for i in range(0,10):
#     print(i+1,"Welcome",end=" ")


# for i in range(0,10):
#     if i%2==1:
#         print(i,end=" ")


# for i in range(1,51,2):
#         print(i,end=" ")


# n=int(input())
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)


# for i in range(20,1,-2):
#     print(i)

# for i in range(20,0,-1):
#     if i%2==0:
#         print(i)

'''
n=int(input())            # 2
sum=0                     #sum=0
for i in range(n):        #i=0            #i=1
    numbr=float(input())  #numbr=10=>10.0 #numbr=5=>5.0
    sum=sum+numbr         #sum=0+8.0=>8.0 #sum=8.0+5.0=>13.0
avg=sum/n
print(avg)

'''

'''
# Counting number of characters in string
strng=input()
count=0
for char in strng:
    count+=1
print(count)

'''

'''
nmbr1=int(input())
nmbr2=int(input())
x=int(input())
y=int(input())
lb=nmbr1 if nmbr1<nmbr2 else nmbr2
ub=nmbr2 if nmbr2>nmbr1 else nmbr1
for num in range(lb,ub+1):
    if num%x==0 and num%y==0:
        print(num)

'''

'''
nmbr1=int(input())
nmbr2=int(input())
x=int(input())
y=int(input())
if nmbr1>=nmbr2:
    nmbr1,nmbr2=nmbr2,nmbr1
for num in range(nmbr1,nmbr2+1):
    if num%x==0 and num%y==0:
        print(num)
'''


'''

# Program to count number of digits in a nmuber
# Method 1
nmbr=int(input())
cnt=0
for dgt in str(nmbr):
    cnt=cnt+1
print(cnt)

'''

'''
nmbr=int(input())
evn_cnt=0
odd_cnt=0
for dgt in str(nmbr):
    if int(dgt)%2==0:
        evn_cnt=evn_cnt+1
    else:
        odd_cnt=odd_cnt+1
print(evn_cnt)
print(odd_cnt)

'''

'''
# count a digit in a given number
nmbr=int(input())
dgt=int(input())
cnt=0
for i in str(nmbr):
    if dgt==int(i):
        cnt=cnt+1
print(cnt)

'''


'''
# Program to count sum of digits in a number
nmbr=int(input())
sum=0
for dgt in str(nmbr):
    sum=sum+int(dgt)
print(sum)

'''

'''
# Reverse of a number
nmbr=int(input())
rev=0
n=0
for dgt in str(nmbr):
    rev=rev+int(dgt)*10**n
    n=n+1
print(rev)

'''

'''

# polindrome of a number
nmbr=int(input())
rev=0
n=0
for dgt in str(nmbr):
    rev=rev+int(dgt)*10**n
    n=n+1
print(1) if nmbr==rev else print(0)
    
'''

'''
# Perfect number
nmbr=int(input())
sum=0
for num in range(1,nmbr):
    if nmbr%num==0:
        sum=sum+num
print(1) if sum==nmbr else print(-1)

'''


'''
# Perfect numbers in a given range
st=int(input())
ed=int(input())
for num in range(st,ed):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print(num)

'''


'''
# Prime num check
nmbr=int(input())
cnt=0
for i in range(2,nmbr):
    if nmbr%i==0:
        cnt=cnt+1
if cnt>0:
    print(0)
else:
    print(1)

'''

'''
# Prime numbers in a given range
st=int(input())
ed=int(input())
for num in range(st,ed):
    cnt=0
    for i in range(2,num):
        if num%i==0:
            cnt=cnt+1
    if cnt==0:
        print(num)

'''
