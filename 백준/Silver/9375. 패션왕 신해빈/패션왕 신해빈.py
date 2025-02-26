import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    clo = {}
    num = int(input().strip())
    for _ in range(num):
        name, type = input().strip().split()
        if type in clo:
            clo[type].append(name)
        else:
            clo[type] = [name]
    
    cnt = 1
    
    for x in clo:
        cnt *= (len(clo[x]) + 1)
	
    print(cnt-1)