# BFS -> 큐 방식으로 구현

from collections import deque
graph = [
    [], [2 ,3 ,8], [1 ,7], [1 ,4 ,5], [3 ,5], [3 ,4], [7], [2 ,6 ,8], [1 ,7]
]

visited = [False]*9
lst=deque()

def bfs(graph,v,visited):
    lst.append(v)
    visited[v]=True

    while lst:
        v=lst.popleft()
        for i in graph[v]:
            if not visited[i]:
                lst.append(i)
                visited[i]=True
        print(v)

bfs(graph,1,visited)