import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    result = a*b

    while b>0:
        a,b = b, a%b
    
    print(result//a)