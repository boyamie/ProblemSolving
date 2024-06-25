import sys
n, m = map(int, sys.stdin.readline().split())
namel = []
for i in range(n+m):
    x = sys.stdin.readline()
    namel.append(x)
hear = set(namel[:n])
see = set(namel[n:])
fin = list(hear & see)
fin.sort()
print(len(fin))
print(''.join(fin), end='')