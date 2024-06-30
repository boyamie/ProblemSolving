def solution(n):
    full = n//7
    if n % 7 > 0:
        full+=1
    return full