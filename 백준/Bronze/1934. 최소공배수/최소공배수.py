import math

def cal(x, y):
    print(x * y // math.gcd(x, y))

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    cal(x, y)
