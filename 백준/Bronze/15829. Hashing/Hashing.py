import sys
input = sys.stdin.readline
l = int(input())
strr = input()
ans = 0

for i in range(l):
    ans += ((ord(strr[i])-96)*(31**i))
print(ans %123456791)