n = int(input())
arr = list(map(float,input().split()))
sum =0.0
average=0
for i in range(n):
    sum +=arr[i]
    average= round(sum/n,1)
print(average)
if average >=4.0:
    print("Perfect")
elif average>=3.0:
    print("Good")
else:
    print("Poor")