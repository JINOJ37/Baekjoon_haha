n = int(input())
li = [input() for _ in range(n)]
li.sort()
li2 = []

for i in range(1, 51):
    for j in range(n):
        if len(li[j]) == i and li[j] not in li2:
            li2.append(li[j])

for i in li2:
    print(i)