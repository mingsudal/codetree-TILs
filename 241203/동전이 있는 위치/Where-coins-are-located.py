# 입력 받기
n, m = map(int, input().split())

# n x n 크기의 격자 생성 (모두 0으로 초기화)
grid = [[0] * n for _ in range(n)]

# 동전 위치 입력 및 격자 업데이트
for _ in range(m):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1  # 격자의 인덱스는 0부터 시작하므로 r-1, c-1

# 격자 출력
for row in grid:
    print(" ".join(map(str, row)))
