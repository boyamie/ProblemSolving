n = int(input())
now = list(map(int, input().split()))
m = max(now)
for i in range(n):
    now[i] = now[i]/m*100
hap = sum(now)
print(hap/n)