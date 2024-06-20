def fi(n):
    if n<=1 :
        return n
    return fi(n-1)+fi(n-2)
print(fi(int(input())))