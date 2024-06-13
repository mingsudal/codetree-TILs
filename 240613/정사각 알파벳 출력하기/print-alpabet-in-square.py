n=int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = 0

for i in range(n):
    for j in range(n):
        print(alphabet[index], end="")
        index += 1
    print()