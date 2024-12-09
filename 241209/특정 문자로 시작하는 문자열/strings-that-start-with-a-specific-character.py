n=int(input())
strings = [input().strip() for _ in range(n)]
target_char = input().strip()
filtered_strings = [s for s in strings if s.startswith(target_char)]
count = len(filtered_strings)
total_length = sum(len(s) for s in filtered_strings)
average_length = total_length / count
print(count, f"{average_length:.2f}")