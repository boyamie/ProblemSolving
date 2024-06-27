def solution(n):
    answer = ''
    
    while(n>=1):
        namozi = n%3
        n = n//3
        answer += str(namozi)
        
    return int(answer, 3)
    