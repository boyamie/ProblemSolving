change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alp = input()

for i in change:
    alp = alp.replace(i, "o")

print(len(alp))    