import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
count = 0

for i in num:
    if i==v: count+=1

print(count)