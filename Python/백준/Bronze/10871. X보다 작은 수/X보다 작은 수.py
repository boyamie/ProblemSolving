n, x = map(int, input().split())
arr = input().split()
new = []
for i in arr:
        if int(i) < x:
                print(i, end = ' ')