def solution(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum