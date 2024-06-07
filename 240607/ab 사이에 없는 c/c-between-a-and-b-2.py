a,b,c=map(int,input().split())
satified = False
if any(i % c == 0 for i in range(a, b + 1)):
    print("NO")
else:
    print("YES")