start,end=map(int,input().split())
cnt = 0
for num in range(start, end + 1):
    sum = 0   
    # 자신을 제외한 약수 계산
    for i in range(1, num):
        if num % i == 0:
            sum += 1
    if sum == 3:
        cnt+=1
print(cnt)