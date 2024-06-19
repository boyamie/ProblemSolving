def solution(arr, queries):
    answer =[]
    for query in queries:
        s,e,k = query
        ans = []
        for i in range(s,e+1):
            if arr[i] > k:
                ans.append(arr[i])
        if len(ans) == 0:
            answer.append(-1)
        else:
            answer.append(min(ans))
    return answer