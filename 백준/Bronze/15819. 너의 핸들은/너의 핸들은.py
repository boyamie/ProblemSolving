import sys
input = sys.stdin.readline
n, i = map(int, input().split())
handle = []
for _ in range(n):
    handle.append(input().rstrip())
handle.sort()
print(handle[i-1])