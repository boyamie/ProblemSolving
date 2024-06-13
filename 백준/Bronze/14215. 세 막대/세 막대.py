num = list(map(int, input().split()))
num.sort()
if num[2] >= num[1]+num[0]:
    num[2] = num[1]+num[0]-1
    print(sum(num))
else:
    print(sum(num))