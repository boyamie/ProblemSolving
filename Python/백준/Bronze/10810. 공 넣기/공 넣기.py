n, m = map(int, input().split())
bag = [0 for i in range(n)] #0개인 바구니 n개
for a in range(m):
    i, j, k = map(int, input().split())
    for a in range(i,j+1):
        bag[a-1]=k
for n in range(n):
    print(bag[n], end = ' ')