import sys
input = sys.stdin.readline
s = input().strip().split('-')
eq = []
for i in s:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    eq.append(cnt)
answer = eq[0]
for i in eq[1:]:
    answer -= i
print(answer)