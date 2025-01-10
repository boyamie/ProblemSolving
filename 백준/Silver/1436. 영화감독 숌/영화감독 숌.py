import sys
input = sys.stdin.readline
n = int(input())
ch = 666
cnt = 0
while cnt < n:
    if '666' in str(ch):
        cnt += 1
    ch +=1
print(ch-1)