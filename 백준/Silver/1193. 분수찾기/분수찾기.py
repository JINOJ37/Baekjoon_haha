x = int(input())
line = 1

while x>line:
    x -= line
    line += 1

if line % 2:
    print(f"{line-x+1}/{x}")

else:
    print(f"{x}/{line-x+1}")