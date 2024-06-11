n=int(input())
plus = 1
minus =n
for i in range(1, 2 * n + 1):
    if i % 2 == 1:
        print("* " * plus)
        plus += 1
    else:
        print("* " * minus)
        minus -= 1