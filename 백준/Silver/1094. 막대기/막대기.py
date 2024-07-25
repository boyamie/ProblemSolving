import sys
input = sys.stdin.readline
x = int(input())
cnt = 0
stick = 0
short = 64
while stick != x:
    if x - stick >= short:
    	stick += short
    	cnt += 1
    short /= 2
print(cnt)