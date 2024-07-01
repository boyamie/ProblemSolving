n = int(input())
all = []
for i in range(n):
    n = input()
    all.append(n)
fi = list(set(all))
fi.sort()
fi.sort(key=len)

for i in fi:
    print(i)