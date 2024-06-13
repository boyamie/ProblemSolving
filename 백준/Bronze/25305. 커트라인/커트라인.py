n, k = map(int, input().split())
score = list(map(int, input().split()))
li = sorted(score)
print(li[-(k)])