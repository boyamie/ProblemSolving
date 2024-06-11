m = int(input())
n = int(input())
sosu = []
for i in range(m, n+1):
    x = 0
    if i > 1:
        not_so = 0
        for j in range(2, i):
            if i % j == 0:
                x += 1
        if x == 0:
            sosu.append(i)
if len(sosu)<1:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))               