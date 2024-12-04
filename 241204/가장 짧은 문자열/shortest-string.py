str1 = input()
str2 = input()
str3 = input()

lengths = [len(str1), len(str2), len(str3)]

difference = max(lengths) - min(lengths)
print(difference)