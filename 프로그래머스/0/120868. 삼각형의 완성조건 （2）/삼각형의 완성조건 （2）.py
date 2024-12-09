def solution(sides):
    answer = 0
    long = max(sides)
    short = min(sides)
    
    for i in range(long-short+1,long+1):
        answer+= 1
        
    for i in range(long+1, long+short):
        answer+=1
    return answer