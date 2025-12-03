def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def modluo(a,b):
    return a%b

def countDigits(n):
    c=0
    while n!=0:
        c+=1
        n//=10
    return c

def sumDigits(n):
    sum=0
    while n!=0:
        sum=sum+n%10
        n//=10
    return sum