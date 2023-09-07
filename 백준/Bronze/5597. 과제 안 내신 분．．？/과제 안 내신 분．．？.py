import sys

list = [0 for _ in range(30)]
for i in range(28):
    k = int(sys.stdin.readline())
    list[k-1] = 1

for i in range(30):
    if list[i]==0: print(i+1)