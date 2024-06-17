arr = list(map(int, input().split()))

for i in range(2, 10): 
    new_arr= (arr[i-1] + arr[i-2])
    if new_arr>=10:
        new_arr-=10
    arr.append(new_arr)
for i in range(len(arr)):
	print(arr[i], end=" ")