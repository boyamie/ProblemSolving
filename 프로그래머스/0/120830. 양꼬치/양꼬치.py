def solution(n, k):
    no = n*12000 + k*2000
    service = n//10 *2000
    return no-service