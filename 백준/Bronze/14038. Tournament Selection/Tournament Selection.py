import sys
input = sys.stdin.readline
cnt = 0
for i in range(6):
    n = input().strip()
    if n == 'W':
        cnt += 1
if cnt >=5:
    print(1)
elif 3<=cnt<5:
    print(2)
elif 1<=cnt<3:
    print(3)
else:
    print(-1)