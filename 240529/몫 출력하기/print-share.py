count = 0  # 반복 횟수를 세는 변수

while True:
    try:
        num = int(input())  # 수를 입력 받음

        if num % 2 == 0:  # 입력값이 짝수인 경우
            print(num // 2)  # 2로 나눈 몫 출력
            count += 1  # 반복 횟수 증가
            if count == 3:  # 반복 횟수가 3이면 종료
                break
    except EOFError:
        break