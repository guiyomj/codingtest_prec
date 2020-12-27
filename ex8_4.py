n=int(input())
ans=0
lst=[0]*1000
lst[1]=1
lst[2]=3
for i in range(3,n+1):
    lst[n] = (lst[n-1]+2*lst[n-2]) % 796796
print(lst[n])