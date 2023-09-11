n, b = map(int, input().split())

def convert10tob(n, b):
    S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = divmod(n, b)
    if q == 0:
        return S[r]
    else:
        return convert10tob(q, b) + S[r]
    
print(convert10tob(n,b))