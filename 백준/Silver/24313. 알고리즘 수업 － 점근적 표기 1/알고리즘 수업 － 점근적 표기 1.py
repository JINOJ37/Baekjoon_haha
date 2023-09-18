a1, a0 = map(int, input().split())
c = int(input())
n = int(input())
flag = 1

for i in range(n, 100):
    if a1*i+a0 > c*i:
        flag = 0
        break

print(flag)
    