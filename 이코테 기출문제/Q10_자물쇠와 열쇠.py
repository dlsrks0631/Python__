# 2차원 리스트 90도 회전 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산 -> 세로 길이
    m = len(a[1]) # 열 길이 계산 -> 가로 길이
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

