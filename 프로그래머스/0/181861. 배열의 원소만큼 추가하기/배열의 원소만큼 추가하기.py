def solution(arr):
    X = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            X.append(arr[i])
    return X