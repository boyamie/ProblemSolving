import sys
input = sys.stdin.readline
n = int(input())
fin = []
for i in range(n):
    b, p, q, r = map(int, input().split())
    score = p*q*r
    rank = p+q+r
    fin.append([b, score, rank])
fin.sort(key=lambda x: (x[1], x[2], x[0]))

for i in range(3):
    print(fin[i][0], end=' ')