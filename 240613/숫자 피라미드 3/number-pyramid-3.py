n=int(input())
for i in range(1,n+1): 
    for j in range(i+1):
        if i*j !=0:
            print(i*j , end=" ")   
    print()