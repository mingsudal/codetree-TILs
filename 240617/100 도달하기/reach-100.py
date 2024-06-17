n = int(input())
a = 1
b = n

result = [a, b]

while True:
    next_term = a + b
    result.append(next_term)
    if next_term > 100:
        break
    
    a = b
    b = next_term

print(" ".join(map(str, result)))