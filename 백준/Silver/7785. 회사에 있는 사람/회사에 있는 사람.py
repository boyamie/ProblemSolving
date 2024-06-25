import sys
n = int(sys.stdin.readline())
of = {}
for i in range(n):
    na, b= map(str, sys.stdin.readline().split())
    if b == 'enter':
        of[na] = True
    else:
        of[na] = False
for i in sorted(of.keys(), reverse=True):
    if of[i]:
        print(i)