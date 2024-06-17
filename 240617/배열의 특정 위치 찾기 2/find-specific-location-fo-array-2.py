arr = list(map(int, input().split()))
sum2 = 0
sum3 = 0

for i in range(10):
    if (i + 1) % 2 == 0:
        sum2 += arr[i]
    if i % 2== 0:
        sum3 += arr[i]



if sum2<sum3:
    print(sum3-sum2)
else:
    print(sum2-sum3)