def solution(n):
    ans = 1
    while 1:
        if 6*ans%n == 0:
            break
        else:
            ans += 1
    return ans