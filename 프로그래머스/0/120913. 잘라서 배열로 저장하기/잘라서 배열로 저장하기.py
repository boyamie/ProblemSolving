def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str),n):
        answer.append(str(my_str[i:i+n]))
    return answer