n,m = map(int, input().split())
bag = [i for i in range(1,n+1)]
for a in range(m):
    i,j = map(int, input().split())
    k = bag[i-1:j]
    k.reverse()
    bag[i-1:j] = k
    
for i in range(n):
    print(bag[i], end=' ')