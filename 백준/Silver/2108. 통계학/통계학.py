import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(round(sum(lst)/n))
print(sorted(lst)[n//2])
from collections import Counter
counter = Counter(lst)
many = counter.most_common()
many.sort(key=lambda x: (-x[1], x[0]))
if len(many)>1 and many[0][1] == many[1][1]:
    mode = many[1][0]
else:
    mode = many[0][0]
print(mode)
print(max(lst)-min(lst))