n,m = map(int,input().split())
a,b,d = map(int,input().split())
maps=list()
arr=[
    [0,-1], [-1,0], [0,1], [1,0]
]
arr2=[
    [1,0], [0,-1], [-1,0], [0,1]
]
ans=1
for i in range(n):
    maps.append(list(map(int,input().split())))

maps[a][b]=999 # 현재 위치

while True:
    if maps[a+arr[d][0]][b+arr[d][1]] == 0: # 갈 수 있는 땅이 있으면?
        a=a+arr[d][0] # 이동한다
        b=b+arr[d][1]
        maps[a][b] = 999
        d += d==0 and 3 or -1  # 방향을 바꾼다
        ans+=1
    elif 0 not in ((a-1>=0 and maps[a-1][b]), (b-1>=0 and maps[a][b-1]), (a+1<n and maps[a+1][b]), (b+1<m and maps[a][b+1])):
        if maps[a + arr2[d][0]][b + arr2[d][1]] == 1:
            break
        else:
            a+=arr2[d][0]
            b+=arr2[d][1]
    else: # 갈 수 있는 땅이 없으면?
        d += d==0 and 3 or -1  # 방향을 바꾼다

print(ans)