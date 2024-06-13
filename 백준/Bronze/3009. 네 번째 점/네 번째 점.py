x_all = []
y_all= []
for i in range(3):
    x, y = map(int, input().split())
    x_all.append(x), y_all.append(y)
for i in x_all:
    if x_all.count(i) == 1:
        finalx = i
for i in y_all:
    if y_all.count(i) == 1:
        finaly = i
print(finalx, finaly)         