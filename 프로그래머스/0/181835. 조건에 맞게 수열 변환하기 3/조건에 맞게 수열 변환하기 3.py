def solution(arr, k):
    if k % 2:
        return [arr[i]*k for i in range(len(arr))]
    else:
        return [arr[i]+k for i in range(len(arr))]