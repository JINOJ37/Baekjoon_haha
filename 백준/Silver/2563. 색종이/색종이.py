n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper[i][j] = 1

count = [a for i in range(100) for j in range(100) if paper[i][j] == 1]
print(len(count))