n=int(input())
square = [[(i+1)*(j+1) for j in range(n)] for i in range(n)]

# 좌우 반전된 배열 생성 및 출력
for i in range(n):
    for j in range(n-1, -1, -1):
        print(square[i][j], end=" ")
    print()