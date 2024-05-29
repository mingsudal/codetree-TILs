total = 0
count = 0

while True:
    n = int(input())
    if n >= 20 and n < 30:
        total += n
        count += 1
    else:
        break

if count != 0:
    print("{:.2f}".format(total / count))