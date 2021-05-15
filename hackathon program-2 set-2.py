T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    arr.reverse()
    print(*arr)