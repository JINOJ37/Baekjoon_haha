n = int(input())
li1 = set(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

for i in range(m):
    if li2[i] in li1:
        print(1, end=" ")
    else: print(0, end=" ")