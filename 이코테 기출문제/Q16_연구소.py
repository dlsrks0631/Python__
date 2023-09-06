'''
!! DFS와 BFS는 언제 사용해야할까
DFS -> 연결된 그래프를 완전 탐색하는데 활용가능
    -> 깊이 우선탐색 알고리즘으로서 우직하게 선택한 한 루트를 파고듬
    -> DFS는 재귀적인 특징과 백트래킹을 이용한, 모든 경우를 하나하나 전부 탐색하는 완전탐색 문제를 풀때 선호(대표적으로 조합 순열 구현)

BFS -> depth(깊이)특징을 이용한 문제(대표적으로 최단경로)를 풀어야할때 선호

+ return --> 함수의 결과값을 반환하기도 하지만 함수를 빠져나가는 기능도 한다
'''

n,m = map(int,input().split())

data = []
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤 맵

# 현재 맵 상태 입력 받음
for _ in range(n):
    data.append(list(map(int,input().split())))

# 방향 설정
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 바이러스 퍼뜨리기 -> DFS 활용
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 상 하 좌 우를 확인했을 때 바이러스가 퍼질 수 있으면
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

# 안전영역 계산
def calculate():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    
    return score

result = 0

def dfs(count):
    global result

    if count == 3:
        # 현재 맵상태를 벽을 설치한 뒤 맵에 넣음
        for i in range(n):
            for j in range(m):
                temp[i][j] == data[i][j]
        
        # 벽을 설치하고
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        
        result = max(result,calculate())
        return # 함수를 빠져나옴

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)