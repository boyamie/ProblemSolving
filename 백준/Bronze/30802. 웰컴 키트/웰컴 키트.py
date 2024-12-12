n = int(input())
ex = list(map(int,input().split()))
t,p = map(int,input().split())

ans = 0
for i in range(len(ex)):
    if ex[i]%t == 0:
        ans += int(ex[i]/t)
    else:
        ans += (int(ex[i]/t)+1)

print(ans)

ans2 = [int(sum(ex)/p),sum(ex)%p]
print(*ans2)