from collections import deque
n,m=map(int,input().split())
lst=[]
x=0
y=0
d=[
    [0,1],[1,0],[-1,0],[0,-1]
]

for i in range(n):
    tlst=[]
    tmp=input()
    for j in range(m):
        tlst.append(int(tmp[j]))
    lst.append(tlst)

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in d:
            nx=x+i[0]
            ny=y+i[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or lst[nx][ny] == 0:
                continue
            if lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y]+1
                queue.append((nx,ny))
    return print(lst[n-1][m-1])

bfs(0,0)