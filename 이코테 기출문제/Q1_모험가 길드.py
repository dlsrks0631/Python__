'''
한 마을에 모험가가 N명이 있다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정
동빈이를 위해 N명의 모험가에 대한 정보가 주어졌을 때, 떠날 수 있는 그룹의 최댓값을 구하시오

< 아이디어 >
공포도보다 현재 그룹 인원이 많거나 같으면 그룹 생성, 생성되면 다시 현재 그룹 인원 초기화
'''

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

result = 0 # 결과값
count = 0

data.sort() 

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0   # 그룹이 생성되면 현재 그룹 인원 초기화

print(result)
