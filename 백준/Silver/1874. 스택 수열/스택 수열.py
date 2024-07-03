import sys
input = sys.stdin.readline
n = int(input())
stack = []

nlst = []
for i in range(n):
    new = int(input())
    nlst.append(new)

cnt = 1
ans = []
tes = 1

for i in nlst:
    while cnt <= i:
        ans.append('+')
        stack.append(cnt)
        cnt+=1
    if stack[-1] >i:
        tes = 0
    if stack[-1] == i:
        ans.append('-')
        stack.pop()
if tes == 1:
    for i in ans:
        print(i)
else:
    print('NO')