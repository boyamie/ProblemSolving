import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    lt = list(map(int, input().split()))
    lt.sort()
    if lt[-2]-lt[1]>=4:
        print('KIN')
    else: print(sum(lt)-max(lt)-min(lt))