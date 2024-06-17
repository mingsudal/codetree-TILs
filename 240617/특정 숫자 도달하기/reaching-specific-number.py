numbers = list(map(int, input().split()))
total_sum = 0
count = 0

found_250 = False

for num in numbers:
    if num >= 250:
        found_250 = True
        break
    total_sum += num
    count += 1

# 만약 250 이상의 숫자가 나타나지 않았다면, 나머지 숫자들을 포함시킴
if not found_250:
    total_sum = sum(numbers)
    count = len(numbers)

# 평균 계산
average = total_sum / count

# 결과 출력
print(total_sum, f"{average:.1f}")