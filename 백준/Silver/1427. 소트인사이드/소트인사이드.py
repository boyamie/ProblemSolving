n = input()
lt = [n[i] for i in range(len(n))]
lt.sort()
print(''.join(reversed(lt)))