import sys
input = sys.stdin.readline
n1,k1,n2,k2 = map(int, input().split())
bis = n1 * k1
eco = n2 * k2
total = bis+eco
print(total)