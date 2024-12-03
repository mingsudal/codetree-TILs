# 입력 받기
n, m = map(int, input().split())

# n x n 격자를 모두 0으로 초기화
grid = [[0] * n for _ in range(n)]

# m개의 점 입력 및 격자 업데이트
for _ in range(m):
    r, c = map(int, input().split())
    grid[r-1][c-1] = r * c  # 점의 크기 = 행 번호 × 열 번호

# 격자 출력
for row in grid:
    print(" ".join(map(str, row)))
