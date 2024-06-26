def solution(array, commands):
    answer =[]
    for i in range(len(commands)):
        i, j, k = commands[i]
        n_1 = array[i-1:j]
        n_1.sort()
        answer.append(n_1[k-1])
    return answer

