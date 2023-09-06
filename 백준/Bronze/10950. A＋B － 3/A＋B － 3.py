T = int(input())
S = []
for i in range(T):
    A, B = map(int, input().split())
    if 0<A<10 and 0<B<10:
        S.insert(i,A+B)
for i in S:
    print(i)