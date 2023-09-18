x, y, z = map(int, input().split())
if (max(x, y, z) == x and x>=y+z):
    print(2*(y+z)-1)
elif (max(x, y, z) == y and y>=x+z):
    print(2*(x+z)-1)
elif (max(x, y, z) == z and z>=y+x):
    print(2*(y+x)-1)
else: print(x+y+z)
    