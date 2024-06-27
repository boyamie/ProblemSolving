import sys
input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
    [x1, y1]= map(int,input().split())
    arr.append([x1,y1])

arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][1])