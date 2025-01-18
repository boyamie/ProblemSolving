import sys
input = sys.stdin.readline
x,y,i = map(int, input().split())
fin = set()

for _ in range(i):
    xll,yll,xur,yur = map(int, input().split())
    for px in range(xll,xur+1):
        for py in range(yll,yur+1):
            fin.add((px, py))
print(len(fin))