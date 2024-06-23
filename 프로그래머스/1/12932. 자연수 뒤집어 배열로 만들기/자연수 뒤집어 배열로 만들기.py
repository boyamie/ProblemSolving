def solution(n):
    answer = [int(str(n)[i]) for i in range(len(str(n)))]
    answer.reverse()
    return answer