n=int(input())
cnt=0
for i in range(n+1): 
    for _ in range(i):
        print(" ",end=" ")
    for j in range(n-i,0,-1):
        print(cnt+1 , end=" ")
        cnt+=1
        if cnt ==9:
            cnt=0   
    print()