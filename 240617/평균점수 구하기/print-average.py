arr = list(map(float,input().split()))
sum =0.0
average=0
for i in arr:
    sum +=i
    average= round(sum/len(arr),1)
print(average)