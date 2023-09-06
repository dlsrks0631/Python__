'''
0과 1로만 이루어진 문자열 S가 있다. 모든 숫자를 전부 같게 만들려고 한다.
다솜이가 할 수 있는 행동은 S네서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.

< 아이디어 >
문자열에서 연속된 0의 그룹 개수와 연속된 1의 그룹 개수를 구한 뒤
0그룹, 1그룹 중 작은 것이 정답이다.

'''

s = input()

group_0 = 0
group_1 = 0

for i in range(len(s)):
    if i != len(s)-1 and s[i] == '0' and s[i+1] == '1':  # index가 마지막일 때를 제외하고 
        group_0 += 1
    elif i == len(s)-1 and s[i] == '0': # index가 마지막일 때 
        group_0 += 1

    elif i != len(s)-1 and s[i] == '1' and s[i+1] == '0':
        group_1 += 1
    elif i == len(s)-1 and s[i] == '1':
        group_1 += 1

result = min(group_0, group_1)
print(result)

##############################################################

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0,count1))
