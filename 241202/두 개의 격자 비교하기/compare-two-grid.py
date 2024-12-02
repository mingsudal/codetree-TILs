# 입력 처리
n, m = map(int, input().split())  # 행의 개수와 열의 개수 입력
array1 = [list(map(int, input().split())) for _ in range(n)]  # 첫 번째 격자 입력
array2 = [list(map(int, input().split())) for _ in range(n)]  # 두 번째 격자 입력

# 두 격자를 비교하여 새 격자 생성
result = [[1 if array1[i][j] == array2[i][j] else 0 for j in range(m)] for i in range(n)]

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
