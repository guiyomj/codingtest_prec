n,m=map(int,input().split())
lst=list()
ans=0
for i in range(n):
    lst.append(int(input()))
d=[9999]*(m+1)
d[0]=0

for i in range(n):
    for j in range(lst[i],m+1):
        if d[j-lst[i]] != 9999:
            d[j]=min(d[j],d[j-lst[i]]+1)

if d[m] == 9999:
    print("-1")
else: print(d[m])
print(d)