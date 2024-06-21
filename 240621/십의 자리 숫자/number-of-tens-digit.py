numbers = list(map(int, input().split()))
# 0이 나타나는 위치까지의 숫자들을 고려
numbers = numbers[:numbers.index(0)]

# 십의 자리 숫자 세기 위한 리스트 (0-9)
counts = [0] * 10

# 각 숫자의 십의 자리 숫자 카운트
for number in numbers:
    if number >= 10:  # 두 자리 수만 고려
        tens_digit = number // 10
        counts[tens_digit] += 1

# 결과 출력
for i in range(1, 10):
    print(f"{i} - {counts[i]}")