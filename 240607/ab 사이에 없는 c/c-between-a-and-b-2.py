a,b,c=map(int,input().split())
satified = False
for i in range(a, b + 1):
    if i % c == 0:
        satified = True
        break

if satified:
    print("YES")
else:
    print("NO")