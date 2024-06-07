a,b,c=map(int,input().split())
satified = False
for i in range(a,b+1):
    if c>i and c%i==0:
        satified=True
    elif c<i and i%c==0:
        satified = True
if satified == True:
    print("YES")
else:
    print("NO")