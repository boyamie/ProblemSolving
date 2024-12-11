import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    a1 = a % 10

    if a1 == 0:
        print(10)
    elif a1 in [1,5,6]:
        print(a1)
    elif a1 in [4,9]:
        b1 = b%2
        if b1 == 0:
            print(a1*a1%10)
        else:
            print(a1)
    else:
        b1 = b%4
        if b1 == 0:
            print(a1** 4 % 10)
        else:
            print(a1 ** b1 %10)