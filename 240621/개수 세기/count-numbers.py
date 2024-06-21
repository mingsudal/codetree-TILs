n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# m의 등장 횟수 세기
count_m = numbers.count(m)

# 결과 출력
print(count_m)