def solution(n):
    if n % 2 == 1:
        return"수박"*int(n//2)+"수"
    else:
        return"수박"*(n//2)