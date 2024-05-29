a = int(input())

for i in range(1, a + 1):
    condition1 = (i % 2 == 0 and i % 4 != 0)
    condition2 = ((i // 8) % 2 == 0)
    condition3 = (i % 7 < 4)
    
    if not (condition1 or condition2 or condition3):
        print(i, end=" ")