'''
백준 14502
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
바이러스의 확산을 막기 위해 연구소에 벽을 세우려고 한다.
연구소의 크기가 N * M인 직사각형으로 나타낼 수 있으며, 직사각형은 1*1 크기의 정사각형으로 나누어져 있다.
연구소는 빈칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지합니다.
일부 칸은 바이러스가 존재하며, 상하좌우로 퍼져나간다.
새로 세울 수 있는 벽의 개수는 3개이다. 안전 영역 크기의 최댓값을 구하시오.

1. 아이디어
- 벽을 3개 설치하는 모든 경우의 수를 다 계산 
- 안전거리 영역 크기를 계산하는 함수 생성
- DFS를 이용해 벽 3개를 설치하는 모든 경우의 수 계산
- 벽을 3개 설치했다면 바이러스를 퍼뜨리고 안전 영역 최댓값 구하기
- DFS 실행해 결과값 출력

2. 시간복잡도
- 64C3 <= 100,000
3. 자료구조
- DFS 활용
'''

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [] # 맵 입력받을 곳
n_graph = [[0] * m for _ in range(n)] # 벽을 설치하고 난 뒤 모습

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 방향 = [상,하,좌,우]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0

# 바이러스 퍼져나감
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if n_graph[nx][ny] == 0:
                n_graph[nx][ny] = 2
                virus(nx,ny)

# 영역 크기 계산
def calculate():
    score = 0
    for i in range(n):
        for j in range(m):
            if n_graph[i][j] == 0:
                score += 1
    return score

# 벽을 설치하면서 안전 영역 크기 계산
def dfs(cnt):
    global result

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                n_graph[i][j] = graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if n_graph[i][j] == 2:
                    virus(i,j)
        
        result = max(result, calculate())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                graph[i][j] = 0
                cnt -= 1

dfs(0)
print(result)



