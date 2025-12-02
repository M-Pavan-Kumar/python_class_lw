#1. Count number of vowels and consonants in a given string
#2. From two strings from given string , the first string contains only vowels and second string conatains only consonants
#3. Merge two strings
#4. String Reverse
#5. polindrome 
#6. Swap letters like uppercase to lowercase and viceversa
#7. remove duplicate words 
#8. remove the duplicate words from the given string


# # 1
# text=input("Enter text : ")
# v_c=0
# c_c=0
# for char in text:
#     if char in "aeiouAEIOU":
#         v_c+=1
#     else:
#         c_c+=1
# print(v_c,c_c)

# # 2
# text=input("Enter text : ")
# v_t=""
# c_t=""
# for char in text:
#     if char in "aeiouAEIOU":
#         v_t+=char
#     else:
#         c_t+=char
# print(v_t,c_t)

# # 3

# text1=input("Enter text : ")
# text2=input("Enter text: ")
# # print(text1+" "+text2)

# # 
# inp=input("enter input: ")
# chara=""
# num=""
# spec=""
# for char in inp:
#     if char.isalpha():
#         chara+=char
#     elif char.isdigit():
#         num+=char
#     else:
#         spec+=char
# print(chara+num+spec) 

# using ascii (A=65,B=66, ... Z=90),(a=97,b=98, ... z=122) ,(0-48,1-49,...,9-57)  
# inp=input("enter input: ")
# chara=""
# num=""
# spec=""
# for char in inp:
#     if 65<=ord(char)<=90  or 97<=ord(char)<=122:
#         chara+=char
#     elif 48<=ord(char)<=57:
#         num+=char
#     else:
#         spec+=char
# print(chara+num+spec) 

# 
# inp=input("enter input: ")
# res=""
# for char in inp:
#     if 65<=ord(char)<=90 :
#         res+=chr(ord(char)+32)
#     elif 97<=ord(char)<=122:
#         res+=chr(ord(char)-32)
# print(res)

# String reverse

# # Using while loop
# n=input("Enter string : ")
# i=len(n)
# res=""
# while i!=0:
#     res+=n[i-1]
#     i-=1
# print(res)

# # using for loop
# n=input("Enter string : ")
# l=len(n)
# res=""
# for i in range(l-1,-1,-1):
#     res=res+n[i]
# print(res)

# 
# n=input("Enter string: ")
# l=len(n)
# res=""
# for i in n:
#     res=i+res
# print(res)

# # Polindrome check
# n=input("Enter string: ")
# l=len(n)
# res=""
# for i in range(l-1,-1,-1):
#     res+=n[i]
# if res==n:
#     print(True)
# else:
#     print(False)


# Removing the duplicates from the strings and counting the number of duplicates
# text=input()
# res=""
# count=1
# for char in text:
#     if char not in res:
#         res+=char
#     else:
#         count+=1
# print("Result string is : ",res)
# print("Count of duplicates is  : ",count)

# counting the words in a string without split()
# strng=input("Enter a string : ")
# count=0
# in_word=False
# for chr in strng:
#     if chr!=" ":
#         if not in_word:
#             count+=1
#             in_word=True
#     else:
#         in_word=False
# print("count of words is : ",count)

# Program to remove spaces from a string

# using replace()
# text=input("Enter the string : ")
# res=text.replace(" ","")
# print(res)

# Witout replace 

# text=input("Enter a string : ")
# res=""
# for chr in text:
#     if chr!=" ":
#         res+=chr
# print(res)


# removing the extra spaces from string

# text=input("Enter a string : ")
# res=""
# in_space=False
# for chr in text:
#     if chr == " ":
#         if  not in_space:
#             res+=chr
#         in_space=True
#     else:
#         res+=chr
#         in_space=False
# print(res.strip())

#  Program to remove duplicate characters without using set
# text=input("Enter string :")
# res=""
# for chr in text:
#     if chr not in res:
#         res+=chr
# print(res)

# Program to find frequency of a specific character
# text=input("Enter a string : ")
# character=input("Enter character : ")
# count=0
# for chr in text:
#     if chr==character:
#         count+=1
# print(count)

# # Character-by-character merge
# text1=input("Enter text : ")
# text2=input("Enter text : ")
# i=0
# res=""
# while i<len(text1) or i<len(text2):
#     if i<len(text1):
#         res+=text1[i]
#     if i<len(text2):
#         res+=text2[i]
#     i+=1
# print(res)

# Program to print each character with its index
# text=input("Enter text: ")
# count=0
# for chr in text:
#     print(f"{chr} -- {count}")
#     count+=1

# # or

# text=input("Enter text: ")
# for i in range(len(text)):
#     print(f"{text[i]} -- {i}")

# # or 
# text=input("Enter text: ")

# for indx,chr in enumerate(text):
#     print(f"{chr} -- {indx}")


#  Program to replace a character in a string manually

text=input("Enter text : ")
old=input("Enter character to replace : ")
new=input("Enter character to add : ")
res=""
for chr in text:
    if chr==old:
        res+=new
    else:
        res+=chr
print("New string is  : ",res)
     
