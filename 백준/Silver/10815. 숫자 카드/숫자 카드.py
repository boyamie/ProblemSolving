import sys
input = sys.stdin.readline
n = int(input())
card = set(map(int,input().split()))
m = int(input())
res = list(map(int, input().split()))
for i in res:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')