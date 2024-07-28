def solution(s):
    answer = ''
    trash = ''
    for i in s:
        if i in trash:
            answer.replace(i, '')
        elif i not in answer:
            answer += i
        elif i in answer:
            answer.replace(i, '')
            trash += i
    lst = list(answer)
    lst.sort()
    fin = []
    for i in range(len(lst)):
        if lst[i] not in trash:
            fin.append(lst[i])
    return "".join(fin)