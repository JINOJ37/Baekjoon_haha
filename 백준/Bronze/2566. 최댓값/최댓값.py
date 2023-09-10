list = [list(map(int, input().split())) for _ in range(9)]
max_n = max(map(max, list))
print(max_n)

index = [(i+1, j+1)  for i in range(9) for j in range(9) if list[i][j] == max_n]
print(f"{index[0][0]} {index[0][1]}")