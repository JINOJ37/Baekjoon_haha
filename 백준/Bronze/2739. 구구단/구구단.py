import sys

n = int(sys.stdin.readline())

if 1<=n<=9:
    for i in range(1,10):
        print(n,"*",i,"=",n*i)