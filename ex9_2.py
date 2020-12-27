# 빠른 다익스트라: 최소 힙 이용 -> O(logn), heapq 라이브러리
import heapq # 일반 리스트 사용
n,m=map(int,input().split())
INF=9999
start=1
graph=[[] for i in range(n+1)]
dist=[INF]*(n+1)
q=[]

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def func(start):
    heapq.heappush(q,(0,start)) # cost, idx
    dist[start]=0

    while q:
        dst, now = heapq.heappop(q)
        if dst > dist[now]: continue

        for i in graph[now]:
            cost=dst+i[1]
            if cost < dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

func(start)
for i in range(1,n+1):
    print(dist[i] == INF and -1 or dist[i])