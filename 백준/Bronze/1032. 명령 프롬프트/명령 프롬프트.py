import sys
input = sys.stdin.readline
n = int(input())
ans = list(input())
for i in range(n-1):
    new = list(input())
    for j in range(len(ans)):
        if ans[j] != new[j]:
            ans[j] = '?'
print(''.join(ans))