while True:
    a, b, c = map(str, input().split())
    a = int(a)
    b = int(b)
    s = a*b
    print(s)
    if c == "C":
        break