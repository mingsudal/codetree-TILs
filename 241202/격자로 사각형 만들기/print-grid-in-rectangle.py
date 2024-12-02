# 입력 받기
n = int(input())

# n x n 크기의 격자 생성
matrix = [[1] * n for _ in range(n)]

# 두 번째 행부터 n번째 행까지 처리
for i in range(1, n):
    for j in range(1, n):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] + matrix[i-1][j-1]

# 출력
for row in matrix:
    print(" ".join(map(str, row)))

