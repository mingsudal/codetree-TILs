n = int(input())
numbers = list(map(int, input().split()))
counts = [0] * 9

for num in numbers:
    if 1 <= num <= 9:
        counts[num - 1] += 1

for count in counts:
    print(count)