'''
BOJ 15686번 치킨 배달

크기가 N * N인 도시가 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 
도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
도시의 치킨 거리가 가장 작게 될지 구하는 프로그램

치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

범위: 2 <= N <= 50 // 1 <= M <=13 

< 문제 해결 >
- 조합 라이브러리를 사용하여 도시에 있는 치킨집 개수 중 M개만큼만 뽑아서 모든 경우의 수에 대하여 도시의 치킨 거리 계산
   -> 그 중 최솟값을 구한다.
- 시간 제한은 1초로 M이 어떤 값이 되더라도 13CM의 값은 100,000을 넘지 않기 때문에 1초 안에 수행 가능하다.

'''
from itertools import combinations

n,m = map(int,input().split())
chicken = []  # 치킨집
house = []  # 집

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m)) # 조합 라이브러리 사용

def get_sum(candidate):
    result = 0
    for hx,hy in house:
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result,get_sum(candidate))
    
print(result)