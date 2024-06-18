n = int(input())
l_1 = set(map(int,input().split()))
m = int(input())
l_2 = list(map(int,input().split()))
for i in l_2:
    if i in l_1:
        print("1")
    else:
        print("0")