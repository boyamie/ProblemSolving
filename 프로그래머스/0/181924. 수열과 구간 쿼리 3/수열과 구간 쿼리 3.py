def solution(arr, queries):
    for i in queries:
        new = i[1]
        new_2 = i[0]
        arr[new], arr[new_2] = arr[new_2], arr[new]
    return arr
