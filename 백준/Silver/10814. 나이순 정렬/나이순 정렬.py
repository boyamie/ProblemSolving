import sys
input = sys.stdin.readline
n = int(input())

lt = []
for i in range(n):
    a,b = input().split()
    lt.append([int(a),b])
lt.sort(key=lambda x:int(x[0]))

for i in lt:
    print(i[0],i[1])