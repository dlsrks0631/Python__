'''
BOJ 18352번 특정 거리의 도시 찾기

어떤 나라에는 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재한다.
모든 도로의 거리는 1이다. 이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
최단거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하시오.

첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
둘째 줄부터 M개의 줄에 거쳐 A,B가 주어지며 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다.
'''

from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)  # 노드 a에서 노드 b까지 간선이 있다

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

q = deque()
q.append(x)

while q:
    now = q.popleft()
    for n_node in graph[now]:
        if distance[n_node] == -1:
            distance[n_node] = distance[now] + 1
            q.append(n_node)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)