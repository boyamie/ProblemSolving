def solution(my_string):
    answer = ''
    mid = [i for i in my_string]
    for i in mid:
        if i not in answer:
            answer += i
    return ''.join(answer)