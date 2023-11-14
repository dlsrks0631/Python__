import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

# 노드 수, 간선 수, 맞는 최단거리, 출발 도시 번호
n, m, target, start = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    A,B = map(int,input().split())
    graph[A].append(B)

distance = [0] * (n+1)
visited = [False] * (n+1)

def bfs(graph, start, visited):
    q = deque([(start)])
    visited[start] = True

    while q:
        x = q.popleft()

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] += distance[x] + 1
   
bfs(graph, start, visited)

result = []
isResult = False
for i in range(1,n+1):
    if distance[i] == target:
        isResult = True
        result.append(i)

if isResult == True:
    for r in result:
        print(r)
else:
    print(-1)

    


    
    
