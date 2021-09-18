x=int(input())
s=[0]*(x+1)
for i in range(2,x+1):
    s[i]=s[i-1]+1
    if s[i] % 2 == 0:
        s[i]=min(s[i],s[i//2]+1)
    if s[i] % 3 == 0:
        s[i]=min(s[i],s[i//3]+1)
    if s[i] % 5 == 0:
        s[i]=min(s[i],s[i//5]+1)
print(s[x])