lt = list(map(int,input().split()))
cnt = 0
for i in lt:
    cnt += i**2
print(cnt%10)