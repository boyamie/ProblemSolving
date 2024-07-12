def solution(s1, s2):
    cnt = 0
    for i in s2:
        for j in s1:
            if i == j :
                cnt += 1
    return cnt