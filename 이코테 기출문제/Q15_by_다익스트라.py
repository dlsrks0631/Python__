'''

 < 다익스트라 알고리즘 >

 - 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘

 1. 출발 노드를 설정
 2. 최단 거리 테이블을 초기화
 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
 5. 위 과정에서 3과 4번을 반복
 
'''

import heapq

INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
                # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
                # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist: continue
                # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for j in graph[now]:
            cost = dist + j[1]
                        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')