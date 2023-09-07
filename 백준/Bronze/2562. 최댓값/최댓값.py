import sys

list = list(map(int, sys.stdin.readlines()))
print(max(list))
print(list.index(max(list))+1)