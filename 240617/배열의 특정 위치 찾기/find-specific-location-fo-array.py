numbers = list(map(int, input().split()))

sum_index = sum(numbers[1::2])

# 3의 배수 번째 값들의 평균 계산
values = [numbers[i] for i in range(2, len(numbers), 3)]
average = sum(values) / len(values) if values else 0

# 평균을 소수 첫째자리까지 반올림하여 출력
print(sum_index, round(average, 1))