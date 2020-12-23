n,m=map(int,input().split())
lst=list()
ans=0

for i in range(n):
    tlst=[]
    tmp=input()
    for j in range(m):
        tlst.append(tmp[j])
    lst.append(tlst)

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if lst[x][y] == '0':
        lst[x][y] = '1'
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            ans+=1
print(ans)