satified = True
for i in range(5):
    n = int(input())
    if n%3 !=0:
        satified=False
        break

if satified == True:
    print(1)
else:
    print(0)