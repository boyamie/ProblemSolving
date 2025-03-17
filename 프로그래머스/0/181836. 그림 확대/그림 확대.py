def solution(picture, k):
    answer = []
    for i in picture:
        new = ""
        for j in i:
            new += j*k
        for i in range(k):
            answer.append(new)
    return answer