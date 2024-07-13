import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = deque()
for i in range(n):
    a = list(map(int,input().split()))
    if a[0] == 1:
        lst.appendleft(a[1])
    elif a[0]==2:
        lst.append(a[1])
    elif a[0] == 3:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())
    elif a[0] == 4:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
    elif a[0] == 5:
        print(len(lst))
    elif a[0] == 6:
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 7:
        if len(lst) != 0:
            print(lst[0])
        else:
            print(-1)
    else:
        if len(lst) != 0:
            print(lst[-1])
        else:
            print(-1)