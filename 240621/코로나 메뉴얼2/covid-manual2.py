people = [input().split() for _ in range(3)]

A_count = 0
B_count = 0
C_count = 0
D_count = 0

# 진료소 분류
for symptom, temp in people:
    temp = int(temp)
    if symptom == 'Y' and temp >= 37:
        A_count += 1
    elif symptom == 'N' and temp >= 37:
        B_count += 1
    elif symptom == 'Y' and temp < 37:
        C_count += 1
    else:
        D_count += 1

# 결과 출력
print(A_count, B_count, C_count, D_count, end=' ')
if A_count >= 2:
    print('E')
else:
    print()