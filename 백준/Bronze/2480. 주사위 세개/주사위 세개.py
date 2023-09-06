A = list(map(int, input().split()))
if A[0]==A[1]==A[2]:
    print("%d" % int(10000+(A[0]*1000)))
elif A[0]==A[1] or A[2]==A[0]:
    print("%d" % int(1000+(A[0]*100)))
elif A[1]==A[2]:
    print("%d" % int(1000+(A[1]*100)))
else:
    money = max(A)*100
    print(money)