import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    x = input().split()
    if x[0] == 'push':
        queue.append(int(x[1]))
    elif x[0] == 'pop':
        if not queue:
            print(-1) 
        else:
            print(queue[0])
            queue.popleft()
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if not queue: print(-1)
        else:
            print(queue[0])
    else:
        if not queue: print(-1)
        else:
            print(queue[-1])