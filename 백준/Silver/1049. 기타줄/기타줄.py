n,m = map(int, input().split())
bundle = []
money = []
for i in range(m):
    pack, ea = map(int, input().split())
    bundle.append(pack)
    money.append(ea)
bundle.sort()
money.sort()
opt1 = (n//6)*bundle[0]+(n%6)*money[0]
opt2 = (n)*money[0]
opt3 = ((n // 6) + 1) * bundle[0]
print(min(opt1,opt2,opt3))