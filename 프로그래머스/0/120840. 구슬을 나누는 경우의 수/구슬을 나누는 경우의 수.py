def solution(balls, share):
    num = 1
    for i in range(share):
        num *= (balls - i)
    pk = 1
    for i in range(1, share+1):
        pk *= i
    answer = num//pk
    return answer