import sys
n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
li2 = sorted(set(li))
di = {li2[i]:i for i in range(len(li2))}

for i in li:
    print(di[i], end=" ")