def solution(strArr):
    ln = [len(list(i)) for i in strArr]
    len_cnt = {}
    for i in ln:
        if i in len_cnt:
            len_cnt[i] += 1
        else:
            len_cnt[i] = 1
    return max(len_cnt.values())