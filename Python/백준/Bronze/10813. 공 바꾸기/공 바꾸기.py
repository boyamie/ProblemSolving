n, m = map(int, input().split())
bag = list(range(1,n+1))
for a in range(m):
    i, j = map(int, input().split())
    q=bag[i-1]
    w=bag[j-1]
    bag[i-1]=w
    bag[j-1]=q
for b in range(n):
    print(bag[b], end =' ')