'''
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력

< 아이디어 >
1차원 배열을 두 개 만들어 이어서 각 배열을 오름차순 정렬 join을 이용하여 문자열을 합침
'''

import sys

input = sys.stdin.readline

number = []
alpha = []

data = input().rstrip()
len = len(data)

for i in range(len):
    if data[i].isdigit():
        number.append(data[i])
    else:
        alpha.append(data[i])

alpha.sort()

sum = 0
for j in number:
    sum += int(j) 

print("".join(alpha)+str(sum))