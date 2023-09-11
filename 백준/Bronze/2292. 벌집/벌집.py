flag = 1
count = 1

n = int(input())
while 1:
    if n<=flag:
        break
    flag += 6*count
    count += 1

print(count)
