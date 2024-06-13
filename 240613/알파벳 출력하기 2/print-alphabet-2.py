n=int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = 0

for i in range(n):
    for _ in range(i):
        print(' ', end=" ")
    for j in range(n-i):
        print(alphabet[index], end=" ")
        index = (index + 1) % 26  

    print()