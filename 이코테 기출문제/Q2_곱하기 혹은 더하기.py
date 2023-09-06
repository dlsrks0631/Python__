'''
각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X'혹은 '+'연산자를 넣어
결과적으로 만들 수 있는 가장 큰 수를 구하는 프로그램. 모든 연산은 왼쪽에서부터 순서대로 이루어짐.

< 아이디어 >
현재 만들어진 값이 1보다 작거나 같으면 data가 1보다 작거나 같으면 곱함
'''

data = input() # int(input())으로 하면 정수값이라 len(data)가 적용이 안됨
sum = 0

for i in range(0,len(data)):
    if int(data[i])<= 1 or sum <= 1:
        sum += int(data[i])
    else:
        sum *= int(data[i])

print(sum)


 