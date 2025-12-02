# Dictionary

# n=int(input("Enter how many items : "))
# d={1:"2",'1':"3",24.5:24.5}
# print(d)
# print(type(d))


# dictionary with integer values from user input
# n=int(input("Enter how many items : "))
# d={}
# for i in range(n):
#     key=input("Enter key : ")
#     value=int(input("Enter value : "))
#     d[key]=value
# print(d)


# Build dictionary using loop until user types "stop"
# d1={}
# while True:
#     key=input("Enter key or (stop): ")
#     if key== "stop":
#         break
#     value=int(input("Enter value : "))
#     d1[key]=value
# print(d1)

# Dictionary created from two user-input lists


# dictionary comprehension
# squares1={x:x*x for x in range(1,6)}
# print(squares1)


# # set
# squares2={x*x for x in range(1,6)}
# print(squares2)

# # 
# s="Apple"
# freq={ch:s.count(ch) for ch in set(s)}
# print(freq)

# # 
# even_squares={i:i*i for i in range(1,11) if i%2==0}
# print(even_squares)


# status={n:("Even" if n%2==0 else "Odd") for n in range(1,6)}
# print(status)


# # clear() - Removes all items
# d={"a":1,"b":2}
# d.clear()
# print(d)

# copy() - create a shallow copy
# d1={"x":10,"y":20}
# d2=d1.copy()
# print(d2)

# fromkeys() - create dict with keys from iterable and common value
# keys=["a","b","c"]
# d=dict.fromkeys(keys,0)
# print(d)

# # get() - return value default if key is missing
# d={"name":"pavan","age":21}
# print(d.get("name"))
# print(d.get("city","NA"))

# items() - returns key value pairs
# d={1:"a",2:"b"}
# print(d.items())

# # keys - returns all the keys
# d={"a":1,"b":2}
# print(d.keys())

# pop() - remove key and returns its value
# d={1:"a",2:"b"}
# print(d.pop(1))

# popitem - remove and returns the last inserted item
# d={1:"a",2:"b"}
# print(d.popitem())


# setdefault() - return value and add key if missing
# d={"name":"Pavan"}
# print(d.setdefault("city","Hyderabad"))
# print(d)

# update() - add the items from another dictionary
# d1={"a":1}
# d2={"b":2}
# d1.update(d2)
# print(d1)

# values() - returns all values
# d={1:"a",2:"b"}
# print(d.keys())


# count frequency of each character
# s=input("Enter a string : ")
# d={}
# for char in s:
#     d[char]=d.get(char,0)+1
# print(d)


# l=[1,2,2,4,5,6,7,2,3,2,3,4,4]
# d={}
# for element in l:
#     d[element]=d.get(element,0)+1
# print(d)

#
# n=int(input("Enter how many items: "))

# d={}
# for i in range(n):
#     name=input("Enter name : ")
#     marks=int(input("Enter marks : "))
#     d[name]=marks
# maxi_key=max(d,key=d.get)
# print(maxi_key,":",d[maxi_key])


# n=int(input("Enter the number of items : "))
# d={}
# for i in range(n):
#     k=input("Enter key : ")
#     v=int(input("Enter value : "))
#     d[k]=v
# dd={}
# for k,v in d.items():
#     dd[v]=k
# print(dd)

# searching for key
n=int(input("Enter the number of items : "))
dd={}
for i in range(n):
    k=input("Enter key : ")
    v=int(input("Enter value : "))
    dd[k]=v

key=input("Enter key to search : ")
if key in dd:
    print("Found")
else:
    print("Not found")





