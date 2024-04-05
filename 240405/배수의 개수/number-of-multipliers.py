even_3 , even_5 = 0,0
for _ in range(10):
    n = int(input())
    if n%3 ==0:
        even_3 +=1
    if n%5 ==0:
        even_5 +=1
print(even_3,even_5)