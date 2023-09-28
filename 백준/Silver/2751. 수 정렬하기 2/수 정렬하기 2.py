import sys
n = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(n)]
list.sort()
for i in list:
    print(i)