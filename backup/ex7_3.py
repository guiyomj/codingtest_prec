n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
start=lst[0]
end=lst[-1]
ans=0

while start <= end:
    mid=(start+end)//2
    s=0
    for i in lst:
        s+=(mid < i and i-mid or 0)
    print("s=",s,"m=",m,"a=",start,"b=",end)
    if s == m:
        ans=mid
        break
    elif s < m: end=mid-1
    else:
        ans=mid
        start=mid+1
print(ans)