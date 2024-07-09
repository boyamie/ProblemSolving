import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())

circ = deque()
for i in range(1, n+1):
    circ.append(i)
ans = []

while circ:
    for i in range(k-1):
        circ.append(circ.popleft())
    ans.append(circ.popleft())

print(str(ans).replace('[','<').replace(']','>'))