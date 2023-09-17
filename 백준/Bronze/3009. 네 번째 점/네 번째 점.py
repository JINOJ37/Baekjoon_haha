spotx = []
spoty = []
for _ in range(3):
    x, y = map(int, input().split())
    if x in spotx: spotx.remove(x)
    else: spotx.append(x)
    if y in spoty: spoty.remove(y)
    else:
        spoty.append(y)

print(spotx[0], spoty[0])