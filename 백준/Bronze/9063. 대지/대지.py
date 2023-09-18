n = int(input())
spotx = list(range(n))
spoty = list(range(n))
for i in range(n):
    spotx[i], spoty[i] = map(int, input().split())

print((max(spotx)-min(spotx))*(max(spoty)-min(spoty)))