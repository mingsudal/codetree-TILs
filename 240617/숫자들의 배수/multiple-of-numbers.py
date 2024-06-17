n=int(input())
cnt =0
value=[]
for i in range(n,100,n):
    if i%5==0:
        cnt+=1
    value.append(i)
    if cnt ==2:
        break
print(" ".join(map(str, value)))