stno=int(input())
if stno>=1 and stno<=90:
    stno=stno%8
    if stno==1:
        print("Lower")
    elif stno==2 or stno==5:
        print("Middle")
    elif stno==3 or stno==6:
        print("Upper")
    elif stno==7:
        print("side lower")
    else:
        print("Side Upper")
else:
    print(-1)