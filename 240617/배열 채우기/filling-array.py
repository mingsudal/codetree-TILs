numbers = list(map(int, input().split()))
lists = []
count = 0

found_0 = False

for num in numbers:
    if num == 0:
        found_0 = True
        break
    lists.append(num)

for i in range(len(lists) - 1, -1, -1):
    print(lists[i], end=" ")