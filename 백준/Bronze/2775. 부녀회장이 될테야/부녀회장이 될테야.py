import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    f_0 = [i for i in range(1,n+1)]
    for floor in range(k): 
        for room in range(1, n):  
            f_0[room] += f_0[room-1]  
    print(f_0[-1]) 