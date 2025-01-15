import sys
input = sys.stdin.readline
n, m = map(int, input().split())

lst = [input().rstrip() for _ in range(n)]
cnt = []

for h in range(n-7):
    for w in range(m-7):
        black = 0
        white = 0
        for i in range(h,h+8):
            for j in range(w,w+8):
                if(i+j)%2 == 0:
                    if lst[i][j] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if lst[i][j] != 'W':
                        black += 1
                    else:
                        white += 1
        cnt.append(white)
        cnt.append(black)
print(min(cnt))