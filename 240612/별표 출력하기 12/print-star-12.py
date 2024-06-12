n=int(input())
for i in range(n):
    if i == 0:
        # 첫 번째 줄은 별을 n개 출력
        print(' '.join(['*'] * n))
    else:
        # 그 외 줄은 간격에 따라 별을 출력
        line = [' '] * (n + (n - 1))
        for j in range(i, len(line), (i + 1) * 2):
            line[j] = '*'
        print(' '.join(line))