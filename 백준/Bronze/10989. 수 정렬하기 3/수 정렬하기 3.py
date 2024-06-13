import sys
n = int(int(sys.stdin.readline()))
lt = [0]*10001

for i in range(n):
    new = (int(sys.stdin.readline()))
    lt[new] += 1

for i in range(10001):
    if lt[i] != 0:
        for j in range(lt[i]):
            print(i)