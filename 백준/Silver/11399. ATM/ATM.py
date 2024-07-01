n = int(input())
jule = list(map(int, input().split()))

jule.sort()
answer = 0

for i in range(1,n+1):
    answer += sum(jule[0:i])
print(answer)