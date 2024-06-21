n=input()
check =[ 'L', 'E', 'B', 'R', 'O', 'S']
idx = -1
for i in range(len(check)):
    if check[i] == n :
        idx =i
if idx == -1:
    print("None")
else:
    print(idx)