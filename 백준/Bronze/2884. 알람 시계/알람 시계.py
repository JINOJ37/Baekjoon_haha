H, M = map(int, input().split())
if 0<=H<=23 and 0<=M<=59:
    if M>=45:
        print("%d %d" % (H,(M-45)))
    else:
        if H==0:
            print("%d %d" % ((H+23),(M+15)))
        else:
            print("%d %d" % ((H-1),(M+15)))