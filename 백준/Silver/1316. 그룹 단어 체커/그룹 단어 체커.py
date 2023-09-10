n = int(input())
number = 0
list = list()

for i in range(n):
    s = input()
    for j in s:
        if j in list and j not in list[-1]:
            number -= 1
            break
        list.append(j)
    number += 1
    list = []

print(number)