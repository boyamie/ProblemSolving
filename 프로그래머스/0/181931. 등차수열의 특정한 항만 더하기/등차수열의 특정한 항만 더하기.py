def solution(a, d, included):
    lt = [a+(i)*d for i in range(len(included))]
    answer = 0
    idx = 0
    for i in included:
        if i == True :
            answer += lt[idx]
            idx += 1
        else:
            idx += 1
    return answer
