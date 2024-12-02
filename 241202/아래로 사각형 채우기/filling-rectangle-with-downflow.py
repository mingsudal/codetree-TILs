n = int(input())

for i in range(1, n + 1):
    row = [str(i + n * (j - 1)) for j in range(1, n + 1)]
    print(" ".join(row))