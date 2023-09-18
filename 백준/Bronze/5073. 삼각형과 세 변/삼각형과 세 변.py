while True:
    x, y, z = map(int, input().split())
    if x==y==z==0:
        break
    elif x==y==z:
        print("Equilateral")
    else:
        if (max(x, y, z) == x and x>=y+z)\
        or (max(x, y, z) == y and y>=x+z)\
        or (max(x, y, z) == z and z>=y+x):
            print("Invalid")
        elif x==y or x==z or y==z:
            print("Isosceles")
        else:
            print("Scalene")