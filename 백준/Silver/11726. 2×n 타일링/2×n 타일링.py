import sys
input = sys.stdin.readline

n = int(input())
anslist = [0]*n
anslist[0] = 1

if n>=2:
  anslist[1] = 2
  for i in range(2,n):
    anslist[i] = anslist[i-1] + anslist[i-2]
print(anslist[n-1]%10007)