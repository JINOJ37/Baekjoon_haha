n = int(input())

for i in range(2*n-1):
    for k in range(abs(n-1-i)):
        print(end=" ")
    if i == n-1:
        k = -1
    for _ in range((n-k-2)*2+1):
        print("*", end="")
    print()