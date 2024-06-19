def solution(arr, queries):
    for i in (queries):
        s,e,k = i
        for x in range(s,e+1):
            if x % k == 0:
                arr[x] += 1
    return arr