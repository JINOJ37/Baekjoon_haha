import sys
n = int(sys.stdin.readline())

list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

list.sort()
for i in range(n):
    print(list[i][0], list[i][1])