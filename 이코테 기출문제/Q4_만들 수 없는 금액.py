'''
동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램

예를 들어, N = 5 이고 3원 2원 1원 1원 9원을 가지고 있을 때
만들 수 없는 양의 정수 금액 중 최솟값은 8원이다

< 아이디어 >
target 보다 큰 data가 나올 시 빠져나옴
'''

n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)