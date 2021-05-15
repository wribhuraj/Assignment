T=int(input())
l=[]
for i in range(T):
    n,m=input().split()
    n=int(n)
    m=int(m)
    arr=list(map(int,input().split(" ")))
    f=0
    for j in range(len(arr)-m+1):
        flag=1
        for k in range(j,j+m):
            if(arr[k]%2==0):
                flag=0
                break
        if(flag==1):
            f=1
            l.append("yes")
            break
    if(f==0):
        l.append('no')
for i in l:
    print(i)