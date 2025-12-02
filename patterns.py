'''

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *


n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print()
for i in range(1,n+1):
    print("* "*n)
'''


'''
* 
* *
* * *
* * * *
* * * * *

n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(1,n+1):
    print("* "*i)


'''

'''
* * * * *
* * * *
* * *
* *
*
n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()

print()

for i in range(1,n+1):
    print("* "*(n-i+1))

'''
'''
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*



n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("*",end=" ")
    print()
print()


for i in range(1,n+1):
    print("* "*i)
for i in range(1,n+1):
    print("* "*(n-i))

'''
'''

#         * 
#       * *
#     * * *
#   * * * *
# * * * * *
n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print()
for i in range(1,n+1):
    print("  "*(n-i),"* "*i)
    
'''
'''
 * * * * *
   * * * *
     * * *
       * *
         *

n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()

print()
for i in range(1,n+1):
    print("  "*(i-1),"* "*(n-i+1))

'''


'''

n=int(input("Enter number of rows : "))
for i in range(1,n):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()

print()
for i in range(1,n):
    print("  "*(n-i),"* "*i)
for i in range(1,n+1):
    print("  "*(i-1),"* "*(n-i+1))

'''

'''

n=int(input("enter rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print()

n=int(input("enter rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

'''

'''
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15



n=int(input("enter rows : "))
p=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(p,end=" ")
        p+=1
    print()

'''
'''

15 14 13 12 11 
10 9 8 7
6 5 4
3 2
1


n=int(input("Enter Rows : "))
p=n*(n+1)//2
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(p,end=" ")
        p=p-1
    print()


'''

'''

A 
B B
C C C
D D D D
E E E E E

n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(i+64),end=" ")
    print()

'''


'''


A 
B C
D E F
G H I J
K L M N O

n=int(input("Enter number of rows : "))
count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(count+64),end=" ")
        count+=1
    print()



'''
'''


A B C D E 
F G H I
J K L
M N
O

n=int(input("Enter number of rows : "))
count=1
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(chr(count+64),end=" ")
        count+=1
    print()



'''

'''

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

n=int(input("Eneter number of rows : "))
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()

    
# or   
n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    print("  "*(n-i),"* "*(2*i-1))

    
'''
'''



* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *

n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()

# or 
n=int(input("Enter number of rows : "))
for i in range(n,0,-1):
    print("  "*(n-i),"* "*(2*i-1))
 
    
    '''
'''

* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()



    '''


'''

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

n=int(input("Eneter number of rows : "))
for i in range(1,n):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()

'''
''' 


5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5


n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(i,end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(i,end=" ")
    print()

'''

'''

1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9


n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(j,end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(j,end=" ")
    print()
'''


'''


5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9

n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(i,end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(j,end=" ")
    print()

'''

'''


E E E E E E E E E 
  D D D D D D D
    C C C C C
      B B B
        A
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E

n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(chr(i+64),end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(chr(i+64),end=" ")
    print()

'''


'''
e e e e e e e e e 
  d d d d d d d
    c c c c c
      b b b
        a
      b b b
    c c c c c
  d d d d d d d
e e e e e e e e e

n=int(input("Eneter number of rows : "))
for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(chr(i+96),end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print(chr(i+96),end=" ")
    print()


'''

'''


*       * 
  *   *
    *
  *   *
*       *

n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    '''

'''
1       1 
  2   2
    3
  4   4
5       5

n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

'''

'''
1       5 
  2   4
    3
  2   4
1       5


n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

'''




'''
3       3 
  2   2
    1
  2   2
3       3


n=int(input("Enter number of rows : "))
mid=n//2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            if i<=mid:
                num=n-i-1
            else:
               num=i-2 
            print(num,end=" ")
        else:
            print(" ",end=" ")
    print()

'''


'''

1       1 
  2   2
    3
  2   2
1       1

n=int(input("Enter number of rows : "))
mid=n//2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            if i<=mid:
                num=i
            else:
               num=n-i+1 
            print(num,end=" ")
        else:
            print(" ",end=" ")
    print()

'''

