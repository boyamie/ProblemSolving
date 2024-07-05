import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    new = int(input())
    if new in dic:
        dic[new] += 1
    else:
        dic[new] = 1
dic = sorted(dic.items(), key = lambda x : (-x[1],x[0]))
print(dic[0][0])