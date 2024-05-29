n = int(input())  # 사용자로부터 정수 n 입력 받음
count = 0  # 나눗셈 횟수를 세는 변수

while n > 1:  # n이 1 이하가 될 때까지 반복
    n //= count + 1  # n을 (count + 1)로 나눔 (1부터 시작하므로 count에 1을 더한 값을 사용)
    count += 1  # 나눗셈 횟수를 증가

print(count)  # 나눗셈 횟수를 출력