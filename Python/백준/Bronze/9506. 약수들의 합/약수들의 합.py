while 1:
    n = int(input())
    if n == -1:
        break
    yak = []
    for i in range(1,n):
        if n%(i) == 0:
            yak.append(i)
    if sum(yak) == n:
        print(n,"=",end=" ")
        print(*yak,sep=" + ")
    else:
        print(n, "is NOT perfect.")