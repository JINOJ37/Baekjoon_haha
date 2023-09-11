t = int(input())
money = [[0 for _ in range(4)] for _ in range(t)]

for i in range(t):
    c = int(input())
    money[i][0], r1 = divmod(c, 25)
    money[i][1], r2 = divmod(r1, 10)
    money[i][2], money[i][3] = divmod(r2, 5)

for i in range(t):
    for j in range(4):
        print(money[i][j], end=" ")
    print()