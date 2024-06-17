numbers = list(map(int, input().split()))

count = 0
total_sum =0
found_0 = False

for num in numbers:
    if num == 0:
        found_0 = True
        break
    total_sum += num
    count += 1


if not found_0:
    total_sum = sum(numbers)
    count = len(numbers)

# 평균 계산
average = total_sum / count

# 결과 출력
print(total_sum, f"{average:.1f}")