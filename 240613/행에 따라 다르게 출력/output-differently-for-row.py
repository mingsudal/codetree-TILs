n = int(input())
cnt=1
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(cnt, cnt + n):
            print(j, end=' ')
        print()
    else:
        for k in range(j + 2, j + 2 + 2 * n, 2):
            print(k, end=' ')  
        cnt = k + 1
        print()