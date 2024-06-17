t = int(input())
for i in range(t):
    total = []
    x = input()
    for j in x:
        if j == '(':
            total.append(j)
        elif j == ')':
            if total:
                total.pop()
            else:
                print("NO")
                break
    else:
        if len(total) == 0:
            print("YES")
        else:
            print("NO")