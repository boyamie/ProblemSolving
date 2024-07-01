import sys
input = sys.stdin.readline
n = int(input())
t= []
for i in range(n):
    a, b = map(int, input().split())
    t.append((a,b))
t.sort(key=lambda x: (x[1],x[0]))
cnt = 1
fi = t[0][1]
for i in range(1, n):
    if t[i][0] >= fi:
        fi = t[i][1]
        cnt += 1

print(cnt)