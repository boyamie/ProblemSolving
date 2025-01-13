import sys
input = sys.stdin.readline
case = int(input())
for i in range(case):
    n, m = map(int, input().split())
    king = list(map(int, input().split()))
    
    num = 1
    while case:
        if king[0] < max(king):
            king.append(king.pop(0))
        else:
            if m == 0:
                break
            
            king.pop(0)
            num += 1
            
        m = m-1 if m>0 else len(king)-1
        
    print(num)