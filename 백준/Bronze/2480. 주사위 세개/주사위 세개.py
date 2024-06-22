a, b, c = map(int, input().split())
x = []
x_2 = []
if a == b == c:
    print(10000+a*1000)
elif a != b and a != c and b != c:
    l = [a,b,c]
    print(int(max(l)*100))
else:
    for i in [a,b,c]:
        if  i not in x:
            x.append(i)
        else:
            if i not in x_2:
                x_2.append(i)
    print(1000+int(x_2[0])*100)       