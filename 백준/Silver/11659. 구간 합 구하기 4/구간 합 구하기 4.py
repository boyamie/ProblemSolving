import sys
n, m = map(int, sys.stdin.readline().split())
n_input = [0]
n_input += list(map(int, sys.stdin.readline().split()))

for i, num in enumerate(n_input):
    if i>0:
        n_input[i] = n_input[i-1] + num

for i in range(m):
    q,p = map(int,sys.stdin.readline().split())
    print(n_input[p]- n_input[q-1])