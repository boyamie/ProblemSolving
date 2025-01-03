import sys
input = sys.stdin.readline
while 1:
    a = input().strip()
    if a == "0":
        break
    if a==a[::-1]:
        print("yes")
    else:
        print("no")