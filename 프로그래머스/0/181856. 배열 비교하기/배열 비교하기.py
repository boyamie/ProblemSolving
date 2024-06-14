def solution(arr1, arr2):
    a, b = len(arr1), len(arr2)
    a_s, b_s = sum(arr1), sum(arr2)
    if a==b:
        if a_s == b_s: return 0
        elif a_s > b_s: return 1
        else: return -1
    elif a > b: return 1
    else: return -1