def solution(array):
    answer = []
    i = max(array)
    answer.append(i)
    a = array.index(answer[0])
    answer.append(a)
    return answer