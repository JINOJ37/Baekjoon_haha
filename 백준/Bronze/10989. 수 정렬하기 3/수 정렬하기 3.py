import sys
n = int(sys.stdin.readline())
list = [0 for _ in range(10001)]
for _ in range(n):
    list[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)