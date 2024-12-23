import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
y=0
for i in range(n):
    if k == 0:
        break
    if k>= lst[i]:
        y += k // lst[i]
        k %= lst[i]
print(y)