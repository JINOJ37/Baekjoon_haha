import sys

list = list()
for _ in range(10):
    n = int(sys.stdin.readline())
    if n%42 not in list:
        list.append(n%42)

print(len(list))