# lst1=[]
# print(lst1)

# lst2=[10,20,30,40]
# print(lst2)

# lst3=list(range(0,10,2))
# print(lst3)

# s="pyhton is very easy "
# lst4=s.split()
# print(lst4) 

# # Accesing the elements
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[5])
# print(l[2:7:2])
# print(l[4::2])
# print(l[3:7])
# print(l[8:2:-2])
# print(l[4:100])

# # nested list
# ll=[1,"a","abc",[22,3,4,5],8,9]
# print(ll)
# print(ll[2])
# print(ll[3][1:3])
# print(ll[3][0])

# # cloning lists
# print("cloning lists")
# ll1=[1,2,3,4,5,6,7,8,9,10]
# ll2=ll1
# ll3=ll1[2:6]
# print(ll1)
# print(ll2)
# print(ll3)

# list operations
# len()
# l1=[1,2,3,4,5]
# print(len(l1))

# # concatenation
# l2=[1,2,3,4,5]
# l3=[6,7,8,9,10]
# print(l2+l3)

# # repetition
# l4=[1,2,3,4,5]
# print(l4*3)
# l5=["hello","world"]
# print(l5*2)

# # max()
# l1=[1,2,3,4,5]
# print(max(l1))

# # min()
# l2=[1,2,3,4,5]
# print(min(l2))

# # sum
# l3=[1,2,3,4,5]
# print(sum(l3))


# List methods
# append()
# count()

# l=[1,2,2,2,3,2,4]
# l.append(6)
# print(l.count(2))
# print(l)

# index()

# l=[1,2,2,2,2,3,3]
# print(l.index(1))
# print(l.index(2))

# insert() - To insert item at a specified index position
# l=[1,2,3,4,5]
# l.insert(1,888)
# l.insert(10,999)
# l.insert(-10,777)
# print(l)


# pop
# l=[1,2,3,4,5]
# print(l.pop())
# print(l.pop(0))
# print(l)

# list comprehension
# l=[x*x*x for x in range(1,11) if x%3==0]
# print(l)
# l=[x*2 for x in range(1,11)]
# print(l)

# l=list(range(1,11))
# ll=[digit for digit in l if digit%2==1]
# print(ll)

# size=int(input("Enter size of list : "))
# lst=[]
# for i in range(1,size+1):
#     element=int(input("Enter the element : "))
#     lst.append(element)
# print(lst)
# sum=0
# for digit in lst:
#     sum+=digit
# print("Sum is : ",sum)

# max and min
# size=int(input("Enter size of list : "))
# lst=[]
# for i in range(1,size+1):
#     element=int(input("Enter the element : "))
#     lst.append(element)
# print(lst)
# max=float("-inf")
# min=float("inf")
# for digit in lst:
#     if max<digit:
#         max=digit
#     if min>digit:
#         min=digit
# print("Minimum : ",min)
# print("Maximum : ",max)

size=int(input("Enter size of list : "))
lst=[]
for i in range(1,size+1):
    element=int(input("Enter the element : "))
    lst.append(element)
print(lst)
rev=[]
for i in range(len(lst),0,-1):
    print(rev)
    rev.append(lst[i])
print(rev)