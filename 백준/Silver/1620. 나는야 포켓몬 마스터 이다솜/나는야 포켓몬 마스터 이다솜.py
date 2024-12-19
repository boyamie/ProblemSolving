import sys
input = sys.stdin.readline
n, m = map(int,input().split())
name = dict()
num = dict()
for i in range(1, n+1):
    na = input().strip()
    name[i] = na
    num[na] = i
for i in range(m):
    find = input().strip()
    if find[0].isalpha():
        print(num[find])
    else:
        print(name[int(find)])