def solution(n):
    answer = [0,1]
    for i in range(2,n+1):
        new = answer[i-2]+answer[i-1]
        answer.append(new)
    final = answer[-1]%1234567
    return final
    