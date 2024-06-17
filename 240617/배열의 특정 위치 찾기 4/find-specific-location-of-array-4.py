numbers = list(map(int, input().split()))

count = 0
total_sum = 0
found_0 = False

for num in numbers:
    if num == 0:
        found_0 = True
        break
    if num % 2 == 0:
        total_sum += num
        count += 1

if not found_0:
    for num in numbers:
        if num % 2 ==0:
            total_sum = sum(num)
            count = len(num)

# 결과 출력
print(count, total_sum)