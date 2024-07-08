import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    ans = sum(int(x) for x in str(i))
    ans += i
    if ans == n:
        print(i)
        break
else:
    print(0)