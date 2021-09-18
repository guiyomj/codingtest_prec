n,k=map(int,input().split())
a=sorted(list(map(int,input().split())),reverse=True)
b=sorted(list(map(int,input().split())),reverse=True)
ans=0

for i in range(k):
    ans+=b[i]
for i in a[:len(a)-k]:
    ans+=i

print(ans)