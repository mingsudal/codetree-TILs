[age_a,sex_a] = input().split()
[age_b,sex_b] = input().split()
if (int(age_a)>=19 or sex_a=="M") or (  int(age_b)>=19 and sex_b == "M"):
    print(1)
else:
    print(0)