import sys
input = sys.stdin.readline
m, n = map(int, input().split())
for i in range(m,n+1):
    if i == 1:
        continue
    for k in range(2,int(i**0.5)+1):
        if i % k == 0:
            break
    else:
        print(i)