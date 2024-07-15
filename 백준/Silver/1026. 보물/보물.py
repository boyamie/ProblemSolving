import sys
input = sys.stdin.readline
n = int(input())
res = 0
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
a_lst.sort()
b_lst.sort(reverse=True)
for i in range(n):
    res += a_lst[i]*b_lst[i]
print(res)