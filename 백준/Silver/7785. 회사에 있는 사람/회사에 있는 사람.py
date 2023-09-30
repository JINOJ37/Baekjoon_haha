n = int(input())
li = {}

for _ in range(n):
    a, b = input().split()
    li[a] = b
    
li2 = [i for i in li if li[i] == 'enter']
li2.sort(reverse=True)
for i in li2:
    print(i)