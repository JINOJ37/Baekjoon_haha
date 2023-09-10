n, m = map(int, input().split())
firstNM = [list(map(int,input().split())) for _ in range(n)]
secondNM = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(firstNM[i][j]+secondNM[i][j], end=" ")
    print()