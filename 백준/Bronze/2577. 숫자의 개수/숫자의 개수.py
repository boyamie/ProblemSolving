import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
resu = a*b*c
for i in range(10):
    print(str(resu).count(str(i)))