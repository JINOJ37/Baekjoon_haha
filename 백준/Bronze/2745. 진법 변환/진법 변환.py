n, b = input().split()
n = n[::-1]
b = int(b)
result = 0

for i in range(len(n)):
    try:
        result += int(n[i])*(b**i)
    except:
        result += (ord(n[i])-55)*(b**i)
        continue

print(result)

***
a,b=map(str,input().split())
print(int(a,int(b)))
***
