def solution(arr):
    if len(arr)==1:
        return [-1]
    m = min(arr)
    arr.remove(m)
    return arr