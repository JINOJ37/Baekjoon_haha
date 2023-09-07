import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

sum = 0
max_n = max(list)
for i in range(n):
    sum += float(list[i]/max_n*100)
print(sum/n)