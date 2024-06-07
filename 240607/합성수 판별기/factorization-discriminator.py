n = int(input())
satisfied = False
for i in range(2, n):
    if n % i == 0:
        is_composite = True
        break

if is_composite:
    print("C")
else:
    print("N")