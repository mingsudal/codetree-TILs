a,b,c = map (int,input().split())
if a >b and b>c:
    print(b)
elif a<b and a>c:
    print(a)
elif c>a and c<b:
    print(c)
elif c>b and b>a:
    print(b)
elif a<c and a>b:
    print(a)
elif c>b and c<a:
    print(c)