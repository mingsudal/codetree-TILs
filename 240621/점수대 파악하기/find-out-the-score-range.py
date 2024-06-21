numbers= list(map(int,input().split()))
numbers= numbers[:numbers.index(0)]
count_num=[0]*11
for number in numbers:
    if number >= 10:  # 두 자리 수만 고려
        score = number // 10
        count_num[score] += 1

# 결과 출력
for i in range(10, 0,-1):
    print(f"{i*10} - {count_num[i]}")