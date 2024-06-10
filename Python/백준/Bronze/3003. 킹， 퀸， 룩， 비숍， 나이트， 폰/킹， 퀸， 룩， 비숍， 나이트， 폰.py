plus_mi = list(map(int, input().split()))
sol = [1, 1, 2, 2, 2, 8]
fix = [0 for i in range(6)]
for i in range(6):
    if plus_mi[i] != sol[i]:
        fix[i] = sol[i] - plus_mi[i]
for i in range(6):
    print(fix[i], end=' ')        