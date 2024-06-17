import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    s = sys.stdin.readline()
    if 'push' in s:
        x = s.split()[1]
        stack.append(x)
    elif 'pop' in s:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in s:
        print(len(stack))
    elif 'empty' in s:
        if stack:
            print(0)
        else:
            print(1)
    elif 'top' in s:
        if stack:
            print(stack[-1])
        else:
            print(-1)