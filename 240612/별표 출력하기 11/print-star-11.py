n = int(input())

for i in range(2*n + 1):
    if i % 2 == 0:
        print("* " * (2*n+1))
    else:
        print("*   " * (n) + "*")