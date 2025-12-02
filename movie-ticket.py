age=int(input())
if age<5:
    print("Free")
elif age>=5 and age<=12:
    print(f"${100}")
elif age>=13 and age<=59:
    print(f"${200}")
else:
    print(f"${120}")