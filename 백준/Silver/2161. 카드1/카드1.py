import sys
input = sys.stdin.readline
n = int(input())
lst = [i for i in range(1,n+1)]
prt = []
for i in range(n):
    mo = lst.pop(0)
    prt.append(mo)
    if lst:
        mov = lst.pop(0)
        lst.append(mov)
for i in prt:
    print(i, end=' ')