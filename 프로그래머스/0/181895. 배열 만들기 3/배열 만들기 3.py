def solution(arr, intervals):
    answer = []
    for ele in intervals:
        a, b = ele
        for i in arr[a:b+1]:
            answer.append(i)
    return answer