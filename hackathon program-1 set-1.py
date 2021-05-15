n=int(input())
arr=list(map(int,input().split(" ")))
colorset=set(arr)
sum=0
for i in colorset:
    sum+=arr.count(i)//2
print(sum)
