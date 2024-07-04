import sys
input = sys.stdin.readline
n,k = map(int, input().split())
arr= [ i for i in range(1,n+1)]
ans = []
idx = k-1
cnt = 1
while 1:
    ans.append(arr[idx])
    arr.remove(arr[idx])
    if not len(arr):
        break
    idx = (idx+k-1)
    if idx >= len(arr):
        idx = idx%len(arr)
print('<', end='')
for i in range(n):
    if i == n-1:
        print(ans[i], end='>')
    else:
        print(ans[i], end=', ')