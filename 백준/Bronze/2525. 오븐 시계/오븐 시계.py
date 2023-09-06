A, B = map(int, input().split())
C = int(input())
if 0<=A<=23 and 0<=B<=59 and 0<=C<=1000:
    H = A+((B+C)/60)
    M = (B+C)%60
    if H>=24:
        print("%d %d" % (H-24,M))
    else:
        print("%d %d" % (H,M))