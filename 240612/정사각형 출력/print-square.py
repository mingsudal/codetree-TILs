n=int(input())
cnt=0
for i in range(n):
    for j in range(n):
        print(i * n + j + 1, end = " ")
    print()