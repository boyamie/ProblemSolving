import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for i in range(n):

    new = sys.stdin.readline().split()

    if new[0] == 'push_front':
        dq.appendleft(new[1])
    elif new[0] == 'push_back':
        dq.append(new[1])
    elif new[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else :
            print(dq[0])
            dq.popleft()
    elif new[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])
            dq.pop()
    elif new[0] == 'size':
        print(len(dq))
    elif new[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif new[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])