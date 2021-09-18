n=int(input())
lst=list(map(int,input().split()))
s=[0]*(n+1)
s[0]=lst[0]
s[1]=max(lst[0],lst[1])
for i in range(2,n):
    s[i]=max(s[i-1],s[i-2]+lst[i])

print(s[n-1])