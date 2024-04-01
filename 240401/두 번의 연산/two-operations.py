a = int(input())
b =0
if a%2 !=0 :
    a+=3
    if a%3 ==0:
        a//=3
        print(a)
    else:
        print(a)

else:
    if a%3 ==0:
        a//=3
        print(a)
    else:
        print(a)