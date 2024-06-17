n=int(input())
number = list(map(int, input().split()))
for num in reversed(number):
    if num%2==0:
        print(num,end=" ")