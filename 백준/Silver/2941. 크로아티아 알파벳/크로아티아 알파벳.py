c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()
check = ""
number = 0

for i in s:
    check += i
    if len(check) == 1 or check == 'dz':
        continue
    else:
        if check in c:
            number += 1
            check = ""
        elif len(check) == 2:
            check = check[1:]
            number += 1
        else:
            check = check[2:]
            number += 2

number += len(check)
print(number)

"""
c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()
for i in c:
    s = s.replace(i, 'a')
print(len(s))
"""
