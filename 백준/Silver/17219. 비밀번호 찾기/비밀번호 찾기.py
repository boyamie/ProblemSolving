dict = {}
n, m = map(int,input().split())
for i in range(n):
    site, pw = input().split()
    dict[site] = pw
for i in range(m):
    n = input()
    print(dict[n])   