def solution(s):
    num = len(s)
    if num % 2 == 1:
        return s[int(num//2)]
    else:
        return s[num//2-1:num//2+1]
    
solution("qwer")