def solution(num, k):
    idx = str(num).find(str(k))
    if idx != -1:
        return idx + 1
    else:
        return -1