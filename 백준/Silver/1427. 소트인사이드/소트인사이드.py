num = input()
list = []

for i in num:
    list.append(int(i))

list.sort(reverse=True)

for i in list:
    print(i, end="")