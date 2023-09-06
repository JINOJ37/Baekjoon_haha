N = int(input())
s = ""
if 4<=N<=1000:
    for i in range(int(N/4)):
        s += "long "
    s += "int"
    print(s)
