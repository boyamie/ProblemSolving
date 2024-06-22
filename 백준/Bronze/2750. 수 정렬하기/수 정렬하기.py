n = int(input())
n_2 = []
for i in range(n):
    n_2.append(int(input()))

n_2 = sorted(n_2)
for i in range(n):
    print(n_2[i])