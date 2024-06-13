import sys
n = int(sys.stdin.readline())
lt = []
for i in range(n):
    lt.append(int(sys.stdin.readline()))
st = sorted(lt)
for i in st:
    print(i)