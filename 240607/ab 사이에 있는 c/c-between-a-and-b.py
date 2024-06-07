a,b,c = map(int,input().split())
if (a % c == 0) or ((a // c + 1) * c <= b):
    print("YES")
else:
    print("NO")