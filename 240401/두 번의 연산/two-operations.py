a = int(input())
b =0
if a%2 !=0 :
    a+=3
    if a%3 ==0 :
        b = a//3
        print(b)
    else:
        print(a)
else:
    print(a)