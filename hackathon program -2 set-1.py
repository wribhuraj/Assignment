import math as m
n=int(input())
arr=list(map(int,input().split(" ")))
for i in arr:
    if((m.ceil(i/5)*5)-i<3 and i>=38):
        print((m.ceil(i/5)*5),end=" ")
    else:
        print(i,end=" ")
