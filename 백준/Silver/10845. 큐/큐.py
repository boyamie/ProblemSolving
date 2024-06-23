from sys import stdin

n = int(stdin.readline())
que = []
for i in range(n):
    name = stdin.readline().split()
    if name[0] == 'push':
        que.append(name[1])
    elif name[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            p = que.pop(0)
            print(p)
    elif name[0] == 'size':
        print(len(que))
    elif name[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif name[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
