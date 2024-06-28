matrix = [list(map(int, input().split())) for _ in range(2)]

row_averages = [sum(row) / 4 for row in matrix]

col_averages = [sum(matrix[i][j] for i in range(2)) / 2 for j in range(4)]

total_average = sum(sum(row) for row in matrix) / 8

print(" ".join(f"{avg:.1f}" for avg in row_averages))
print(" ".join(f"{avg:.1f}" for avg in col_averages))
print(f"{total_average:.1f}")