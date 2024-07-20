def solution(array):
    cnt = 0
    for i in array:
        cnt += str(i).count('7')
    return cnt