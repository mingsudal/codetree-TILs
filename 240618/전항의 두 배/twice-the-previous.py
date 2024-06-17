arr=list(map(int,input().split()))
for i in range(2, 10): 
    new_arr=arr[i-1]+2*arr[i-2]
    arr.append(new_arr)
print(" ".join(map(str, arr)))