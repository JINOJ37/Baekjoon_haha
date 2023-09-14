list = list()

while True:
    n = int(input())
    list = []
    if n == -1:
        break

    for i in range(1, n):
        if n%i == 0:
            list.append(i)
    
    if n == sum(list):
        print(f"{n} = ", end = "")
        for i in list:
            if i == list[-1]:
                print(i)
            else:
                print(i, end=" + ")
    else:
        print(f"{n} is NOT perfect.")