import sys
input=sys.stdin.readline
while 1:
    line = input().strip()
    if line == '0 0 0':
        break
    a, b, c = map(int, line.split())
    byn = [a,b,c]
    byn.sort()
    if byn[0]**2 + byn[1]**2 == byn[2]**2:
        print('right')
    else:
        print('wrong')