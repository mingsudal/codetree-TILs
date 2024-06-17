numbers = list(map(int, input().split()))


result = []


for num in numbers:
    if num == 0:
        break
    if num % 2 == 0:
        result.append(num // 2)  
    else:
        result.append(num + 3)   

print(" ".join(map(str, result)))