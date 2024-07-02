import sys
input = sys.stdin.readline
n = int(input())
pyo = []
for i in range(n):
    x, y = map(int, input().split())
    pyo.append([x,y])

pyo.sort(key=lambda x: (x[1],x[0]))
for i in pyo:
    print(i[0], i[1])