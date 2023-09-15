m = int(input())
n = int(input())
list = list()

for i in range(m, n+1):
    if i == 1: continue
    for j in range(2,i+1):
        if i%j == 0 and j!=i:
            break
    if j==i: list.append(i)

if len(list)==0: print("-1")
else:
    print(sum(list))
    print(min(list))