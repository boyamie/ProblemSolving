def solution(n):
    i = 1
    res = 1
    while 1:
        if res > n:
            break
        i += 1
        res *= i
    return i-1