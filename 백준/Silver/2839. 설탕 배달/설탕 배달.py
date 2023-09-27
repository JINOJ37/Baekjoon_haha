n = int(input())
result = n

for i in range(int(n/3+1)):
    j = int((n-3*i)/5)
    if 3*i + 5*j == n:
        result = min(result, i+j)

if result == n: print(-1)
else: print(result)