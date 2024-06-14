def solution(todo_list, finished):
    answer = []
    for i, j in enumerate(finished):
        print(j)
        if j == False:
            answer.append(todo_list[i])
    return answer