def solution(num_str):
    lt = [i for i in num_str]
    answer=0
    for i in lt:
        answer += int(i)
    return answer    