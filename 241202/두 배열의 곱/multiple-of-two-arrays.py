# 입력 받기
array1 = [list(map(int, input().split())) for _ in range(3)]
input()  # 줄 간격 처리
array2 = [list(map(int, input().split())) for _ in range(3)]

# 두 배열의 곱 계산
result = [[array1[i][j] * array2[i][j] for j in range(3)] for i in range(3)]

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
