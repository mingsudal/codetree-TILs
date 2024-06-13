n=int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = 0

for i in range(1,n+1):
    for j in range(i):
        print(alphabet[index], end="")
        index = (index + 1) % 26  
    print()