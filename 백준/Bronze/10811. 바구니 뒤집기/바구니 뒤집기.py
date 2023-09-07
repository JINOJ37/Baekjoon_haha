import sys

n, m = map(int, sys.stdin.readline().split())
list = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp = list[i-1:j][::-1]
    list[i-1:j] = temp

for i in list:
    print(i, end=" ")