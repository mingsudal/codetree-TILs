n=int(input())
arr = list(map(int, input().split()))
new_arr=[]
for i in arr:
    new_arr.append(i*i)
for i in range(len(arr)):
    print(new_arr[i],end=" ")