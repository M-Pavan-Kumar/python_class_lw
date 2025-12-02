#  Program to Find the Length of a List (Without Using Predefined Functions)
# lst=list(map(int,input("Enter values : ").split()))
# cnt=0
# for num in lst:
#     cnt+=1
# print("List is : ",lst)
# print("Length of the list is : ",cnt)

#  Program to Reverse a List Manually (Without Using Predefined Functions)
# lst=lst=list(map(int,input("Enter values : ").split()))
# strt=0
# end=len(lst)-1
# while strt<end:
#     lst[strt],lst[end]=lst[end],lst[strt]
#     strt+=1
#     end-=1
# print(lst)

# Program to Copy a List Manually (Without Using Predefined Functions)
# lst=["apple","banana","orange"]
# copy=[]
# for i in range(len(lst)-1,-1,-1):
#     copy+=[lst[i]]
# print(copy)


# Program to Merge Two Lists Manually (Without Using Predefined Functions)
# l1=list(map(int,input("Enter values : ").split()))
# l2=list(map(int,input("Enter values : ").split()))
# merged_list=[]
# for item in l1:
#     merged_list+=[item]
# for item in l2:
#     merged_list+=[item]
# print(merged_list)

# . Program to Create Separate Even and Odd Lists from a Given List (Without Using Predefined Functions)

# lst=list(map(int,input("Enter values : ").split()))
# even=[]
# odd=[]
# for digit in lst:
#     if digit%2==0:
#         even+=[digit]
#     else:
#         odd+=[digit]
# print("Even list : ",even)
# print("Odd list : ",odd)





# count number of words in a text
# text=input("Enter the text : ")
# words=text.split()
# print(words)
# print("Number of words : ",len(words))

# captializing the first first letter in each word
# for i in range(len(words)):
#     words[i]=words[i].capitalize()
# print(words)

# # captializing the first first letter in each word
# re=[]
# nw=""
# for word in words:
#     for i in range(len(word)):
#         if i==0:
#             nw=word[i].upper()
#         elif i==len(word)-1:
#             nw+=word[i].upper()
#         else:
#             nw+=word[i]
#     re.append(nw)
# print(re)



# # converting all vowels in the words into capital letters
# res=[]
# for word in words:
#     wrd=""
#     for chr in word:
#         if chr in "aeiouAEIOU":
#            wrd+= chr.upper()
#         else:
#             wrd+=chr
#     res.append(wrd)
# print(" ".join(res))


# Remove duplicates from the list
# l=list(map(int,input("Enter elements : ").split()))
# res=[]
# for digit in l:
#     if digit not in res:
#         res.append(digit)
# print(res)


# display unique elements in a list
# l1=list(map(int,input("Enter elements : ").split()))
# l2=list(map(int,input("Enter elements : ").split()))
# new=[]
# for digit in l1+l2:
#     if digit not in l2:
#         new.append(digit)
#     if digit not in l1:
#         new.append(digit)
# print(new)
# print(list(set(l1)&set(l2)))

# sort a list of elements

# l=list(map(int,input("Enter elements : ").split()))
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# Second largest element in a list
# lst=list(map(int,input("Enter elements : ").split()))
# lrgst=scndlrgst=float("-inf")
# for digit in lst:
#     if digit>lrgst:
#         scndlrgst=lrgst
#         lrgst=digit
#     elif digit>scndlrgst and digit!=lrgst:
#         scndlrgst=digit
# print("Largest is : ",lrgst)
# print("Second largest is : ",scndlrgst)


#  frequency count of each element in a list

# lst=list(map(int,input("Enter elements : ").split()))
# freq={}
# for element in lst:
#     if element in freq:
#         freq[element]+=1
#     else:
#         freq[element]=1
# print(freq)

# lst=list(map(int,input("Enter elements : ").split()))
# l=[]
# r=[]
# for elmnt in lst:
#     if elmnt not in l:
#         count=0
#         for el in lst:
#             if elmnt==el:
#                 count+=1
#         r.append((elmnt,count))
#         l.append(elmnt)
# print(r)
# for e,cnt in r:
#     print(e,":",cnt)

#  search a given element in a list
# lst=list(map(int,input("Enter elements : ").split()))
# srch=int(input("Enter element : "))
# indx=-1
# for element in lst:
#     indx+=1
#     if element==srch:
#         print(f"Found element {srch} at index {indx}")
#         break
# else:
#     print("element not found")


# Matrices

# rows=int(input("Enter number of rows: "))
# cols=int(input("Enter number of columns :"))
# matrix=[]
# c=0
# for i in range(rows):
#     row=list(map(int,input(f"Enter elements for {c} row :").split()))
#     c+=1
#     matrix.append(row)
# print(matrix)

# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j],end=" ")
#     print()

# rows=int(input("Enter number of rows: "))
# cols=int(input("Enter number of columns :"))
# matrix=[list(map(int,input(f"Enter elements for row :").split())) for i in range(rows)]
# print("Your output matrix is : ")
# res=[row for row in matrix]
# print(res)

# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]
# B=[]
# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     B.append(row)
# res=[]
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(A[i][j]+B[i][j])
#     res.append(row)
# print(res)

'''
for i in range(rows):
    for j in range(cols):
        print(A[i][j]+B[i][j],end=" ")
    print()
'''
# Transpose of a matrix

# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# for i in range(rows):
#     for j in range(rows):
#         print(A[j][i],end=" ")
#     print()


# # sum of diagonal elements
# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# sum=0
# for i in range(rows):
#     for j in range(rows):
#         if i==j:
#             sum+=A[i][j]
# print("sum of diagonal elements is : ",sum)

# sum of diagonal elements
# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# sum=0
# for i in range(rows):
#     for j in range(rows):
#         if i+j==2:
#             sum+=A[i][j]
# print("sum of diagonal elements is : ",sum)


# Upper triangular matrix
# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# sum=0
# for i in range(rows):
#     for j in range(rows):
#         if i>j:
#             A[i][j]=0

# for i in range(rows):
#     for j in range(rows):
#         print(A[i][j],end=" ")
#     print()

# lower triangular matrix
# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# sum=0
# for i in range(rows):
#     for j in range(rows):
#         if i<j:
#             A[i][j]=0

# for i in range(rows):
#     for j in range(rows):
#         print(A[i][j],end=" ")
#     print()

# lower triangular matrix
# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# sum=0
# for i in range(rows):
#     for j in range(rows):
#         if i<j:
#             print("0",end="")
#         else:
#             print(A[i][j],end=" ")
#     print()

# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# A=[]

# Sum of main and opposite diagonal elements of a matrix 
# A=[]
# rows=int(input("Enter rows: "))
# cols=int(input("Enter columns :"))
# for r in range(rows):
#     row=list(map(int,input(f"Enter elements for row :").split()))
#     A.append(row)
# print()
# sum=0
# for i in range(rows):
#     for j in range(rows):
#         if i+j==row-1 or i==j:
#             sum+=A[i][j]
# print("sum of diagonal elements is : ",sum)

# Corner Elements Sum of a Matrix

# A=[]
# rows=int(input("Enter nuumber of rows : "))
# cols=int(input("Enter nuumber of columns : "))
# for i in range(rows):
#     row=list(map(int,input("Enter the elements for row : ").split()))
#     A.append(row)
# # print(A)
# sum=0
# for i in range(rows):
#     for j in range(cols):
#         if (i==0  and j==rows-1) or (i==0 and j==0) or (i==rows-1 and j==0) or (i==rows-1 and j==cols-1):
#             sum+=A[i][j]
# print("corner Elements Sum of a Matrix is : ",sum)


# Boundary Elements Sum of a Matrix
# A=[]
# rows=int(input("Enter nuumber of rows : "))
# cols=int(input("Enter nuumber of columns : "))
# for i in range(rows):
#     row=list(map(int,input("Enter the elements for row : ").split()))
#     A.append(row)
# # print(A)
# sum=0
# for i in range(rows):
#     for j in range(cols):
#         if i==0 or i==rows-1 or j==0 or j==cols-1:
#             sum+=A[i][j]
# print("Boundary Elements Sum of a Matrix is : ",sum)


# Sparse matrix check 
# A=[]
# rows=int(input("Enter number of rows : "))
# cols=int(input("Enter number of cols : "))
# ttl_elmnts=rows*cols
# for i in range(rows):
#     row=list(map(int,input("Enter the elements for the row : ").split()))
#     A.append(row)
# zr_cnt=0
# for i in range(rows):
#     for j in range(cols):
#         if A[i][j]==0:
#             zr_cnt+=1
# if zr_cnt>ttl_elmnts/2:
#     print("sparse matrix")
# else:
#     print("Not a sparse matrix")


#  Check if a Matrix is Identity Matrix

# A=[]
# rows=int(input("Enter number of rows : "))
# cols=int(input("Enter number of cols : "))
# is_idntty=True
# for i in range(rows):
#     row=list(map(int,input("Enter the elements for the row : ").split()))
#     A.append(row)

# for i in range(rows):
#     for j in range(cols):
#         if i==j:
#             if A[i][j]!=1:
#                 is_idntty=False
#                 break
#         else:
#             if A[i][j]!=0:
#                 is_idntty=False
#                 break
# if is_idntty:
#     print("Identity matrix")
# else:
#     print("Not a Identity matrix")


# Symmetrix matrix check
# A=[]
# rows=int(input("Enter number of rows : "))
# cols=int(input("Enter number of cols : "))
# for i in range(rows):
#     row=list(map(int,input("Enter the elements for the row : ").split()))
#     A.append(row)

# is_symm=True
# if rows!=cols:
#     is_symm=False
# else:
#     for i in range(rows):
#         for j in range(cols):
#             if A[i][j]!=A[j][i]:
#                 is_symm=False
#                 break

# if is_symm:
#     print("Symmetric Matrix")
# else:
#     print("Not a Symmetric Matrix")






 



        
