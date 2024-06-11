n, k = map(int, input().split())
li = [i for i in range(1,n+1)]
yak = []
for i in li:
    if n%i == 0:
        yak.append(i)

if k > len(yak):
    print(0)
else:
    print(yak[k-1])    