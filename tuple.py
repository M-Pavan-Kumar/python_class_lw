# n=int(input("Enter how many values : "))
# t=()
# for i in range(n):
#     val=int(input("Enter value : "))
#     t+=(val,)
# print(t)

# t1=tuple(map(int,input("Enter values for tuple  : ").split()))
# print(t1)

# accessing elements of a tuple 
# A=(5,10,15,20,10)
# print(A[0])
# print(A[1])
# print(A[2:3])
# print(len(A))
# x=5
# print(x in A)

# print(A.count(10))
# print(A.index(10))

# # concatenating the two tuples
# t1=(1,2,3)
# t2=(4,5,6)
# c=t1+t2
# print(c)
# print(t1*3)

# A=(10,20,30)
# l=list(A)
# print(l)
# t=tuple(l)
# print(t)


# max and min in tuple
# A=(22,5,17,9)
# print(max(A))
# print(min(A))
# # Reversing tuple
# print(A[::-1])

# tuple slicing

# A=(22,5,17,9)
# print(A[0:3])

# nested tuple access
# A=(22,(1,2,3),5,17,9)
# print(A[1])
# print(A[1][1])

# checking tuple immutability
# A=(22,3,2,5,4)
# A[1]=200  --> this will give error

# sum of all the elements in a tuple
# A=(22,3,2,5,4)
# print(sum(A))

# tuple of string - find the length of a string
# A=("apple","banana","kiwi")
# for elem in A:
#     print(len(elem))


# Tuple sorting  (convert to list)
# A=(40,20,30,50)
# l=list(A)
# l.sort()
# print(tuple(l))

# compare the two tuples
# A=(10,20,30)
# B=(10,20,30)
# print(A==B)
# print(A is B)

# *a,b=1,2,3,4
# print(a,b)

# x=(1,2,3,4)
# a,b,c,d,e=x
# print(a)
# print(a)
# print(d)
# print(e)

# t=(10,20,30,40,50)
# print(t[:2]+t[3:])

# sets
# s1={}
# s2={10}
# s3=set()
# print(type(s1))
# print(type(s2))
# print(type(s3))

# n=int(input("enter how many elements : "))
# s=set()
# for i in range(n):
#     elem=int(input("Enter a number : "))
#     s.add(elem)

# print(s)

# s=set(map(int,input("enter values : ").split()))
# print(s)

# add single element
# A={10,20,30}
# A.add(40)
# print(A)
# A.add(30)
# print(A)

# update() - add multiple values
# A={1,2}
# A.update([3,4,5])
# print(A)

# remove() - remove element (error if not found)
# A={10,20,30}
# A.remove(20)
# print(A)

# discard() - remove element (no error if not found)
# A={10,20,30}
# A.discard(220)
# print(A)


# pop() - removes and returns the random element

# A={10,20,30,40}
# x=A.pop()
# print("Popped : ",x)
# print(A)


# clear() - removes all elements
# A={10,20,30}
# A.clear()
# print(A)

# copy() - returns a shallow copy

# A={10,20,30}
# B=A.copy()
# print(B)

# union() - return union of sets
# A={10,20,30}
# B={30,40,50} 
# print(A.union(B))

# intersection() - return intersection of sets
# A={10,20,30}
# B={20,40,60} 
# print(A.intersection(B))

# symmetric_difference() - elements not common in both

# A={1,2,3}
# B={3,4,5}
# print(A.symmetric_difference(B))

# issubset() - Check if a is subset of b
# A={1,2}
# B={3,2,1}
# print(A.issubset(B))

#  issuperset() - Check if a is superset of b

# A={1,2}
# B={3,2,1}
# print(B.issuperset(A))

# isdisjoint() - check if sets have no common elements
# A={10,20,30}
# B={40,50}
# print(A.isdisjoint(B))


# enumerate() :
# nums=[10,20,30]
# res=list(enumerate(nums))
# print(res)
# print()

# names=["pavan","kumar","maruboina"]
# for index,name in enumerate(names,start=100):
#     print(index,":",name)



# find the duplicates elements in a set using set and output is list
# res=[]
# elements=list(map(int,input("Enter elements for the set : ").split()))
# non_dupli=set()
# dupli=set()

# for i in elements:
#     if i not in non_dupli:
#         non_dupli.add(i)
#     else:
#         dupli.add(i)
# print(list(dupli))


# Find the common elements in three lists
# l1=list(map(int,input("Enter elements for the set : ").split()))
# l2=list(map(int,input("Enter elements for the set : ").split()))
# l3=list(map(int,input("Enter elements for the set : ").split()))
# print(set(l1) & set(l2) & set(l3))
# r1=set(l1).intersection(set(l2))
# res=r1.intersection(set(l3))
# print(res)

# find all the pairs from two sets whose sum is even

# set1=set(map(int,input("Enter elements : ").split()))
# set2=set(map(int,input("Enter elements : ").split()))
# # res=[]
# res=set()
# for i in list(set1):
#     for j in list(set2):
#         if (i+j)%2==0:
#             res.add((i,j))
# print(res)

set3=set(map(int,input("Enter elements : ").split()))
set4=set(map(int,input("Enter elements : ").split()))

ress1={(i,j) for j in list(set4) for i in list(set3) if (i+j)%2==0}
ress2=set([(i,j) for j in list(set4) for i in list(set3) if (i+j)%2==0])

print(ress1)
print(ress2)

