n = int(input())
list = list(map(int, input().split()))
flag, count = 0, 0

for i in list:
    for j in range(2, i):
        if i % j == 0 and i != j:
            flag = 1
            break
    if i == 1 or flag == 1: 
        flag = 0
    else: count += 1

print(count)
