n = int(input())
a =0 
b= 1
for i in range(n): 
    if i % 2 == 0:
        for j in range(n-a):
            print("* ", end="")
        a+=1
        print()
    else:
        print("*")

for i in range(n):
    if i % 2 == 0:
        for j in range(b+1):
            print("* ", end="")
        b+=1
        print()
    else:
        print("*")