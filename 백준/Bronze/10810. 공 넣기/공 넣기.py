import sys

n, m = map(int, sys.stdin.readline().split())
list = [0 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for l in range(i-1,j):
        list[l] = k

for i in list:
    print(i, end=" ")