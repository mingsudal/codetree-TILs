import re
a=str(input())
b=str(input())
count = len(re.findall(f"(?={re.escape(b)})", a))
print(count)
