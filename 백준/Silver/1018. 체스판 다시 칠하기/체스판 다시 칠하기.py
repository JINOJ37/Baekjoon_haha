n, m = map(int, input().split())
chess = [list(map(str, input())) for _ in range(n)]
result = n*m

for i in range(0, n-7):
    for j in range(0, m-7):
        count1, count2 = 0, 0
        temp1, temp2 = 'B', 'W'
        for k in range(i, i+8):
            for l in range(j, j+8):
                if chess[k][l] != temp1:
                        count1 += 1
                if chess[k][l] != temp2:
                        count2 += 1
                if l == j+7: continue
                else:
                    if temp1 == 'W' : temp1 = 'B'
                    else: temp1 = 'W'
                    if temp2 == 'W' : temp2 = 'B'
                    else: temp2 = 'W'
        result = min(result, count1, count2)

print(result)