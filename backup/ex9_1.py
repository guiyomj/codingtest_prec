# 다익스트라 최단 걍로 알고리즘 : 음의 간선 X, 한 단계에 대한 하나의 노드에 대한 최단 거리를 확실히 찾는 방법, O(n^2);n은 노드의 갯수
INF=9999
n,m=map(int,input("n과 m 입력: ").split()) # n: 노드, m: 간선
start=1
graph=[[] for i in range(n+1)] # 그래프
visited=[False]*(n+1) # 방문 여부
dist=[INF]*(n+1) # 각 노드 사이의 최단거리 저장

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def get_smallest():
    min_value=INF
    idx=0
    for i in range(1,n+1):
        if dist[i] < min_value and not visited[i]:
            min_value=dist[i]
            idx=i
    return i

def dijkstra(start):
    dist[start]=0
    visited[start]=True
    for i in graph[start]:
        dist[i[0]]=i[1]
    for i in range(n-1):
        now=get_smallest()
        visited[now]=True
        for j in graph[now]:
            cost=dist[now]+j[1]
            if cost < dist[j[0]]:
                dist[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
    if dist[i] == INF:
        print("-1")
    else: print(dist[i])