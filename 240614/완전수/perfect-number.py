start,end=map(int,input().split())
cnt = 0
for num in range(start, end + 1):
    sum_of_divisors = 0
    
    # 자신을 제외한 약수의 합을 계산
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    # 완전수인 경우 cnt 증가
    if sum_of_divisors == num:
        cnt += 1

print(cnt)