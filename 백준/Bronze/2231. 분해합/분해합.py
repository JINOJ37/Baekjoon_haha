n = int(input())
result = n

for i in range(1, n):
    k = n-i
    for j in range(len(str(n-i))):
        k += int(str(n-i)[j])
    if k==n:
        result = min(result, n-i)

if result == n:
    print(0)
else: print(result)