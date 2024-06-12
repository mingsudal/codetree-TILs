n=int(input())
cnt=1
for i in range(n):
    for _ in range(n):
        if cnt<10:
            print(cnt,end="")
            cnt+=1
        else:
            cnt=1
            print(cnt,end="")
            cnt+=1
    print()