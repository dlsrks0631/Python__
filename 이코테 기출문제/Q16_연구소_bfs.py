'''
import copy

복사받고 싶은 리스트 = copy.deepcopy(복사하고 싶은 리스트)

a = [1,2,3,4]
b = copy.deepcopy(a) -> b = [1,2,3,4]

'''

from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    #queue에 2의 위치 전부 append
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i,k))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < n and 0 <= ny < m:
            if test_map[nx][ny] == 0:
                test_map[nx][ny] =2
                queue.append((nx,ny))

    global result
    count = 0
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count +=1

    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                make_wall(count+1)
                lab_map[i][k] = 0


n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)