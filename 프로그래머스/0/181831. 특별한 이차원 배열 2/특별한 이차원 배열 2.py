def solution(arr):
    for i,k in enumerate(arr):
        for j in range(len(k)):
            if arr[i][j] != arr[j][i]:
                return 0
        else:
            return 1