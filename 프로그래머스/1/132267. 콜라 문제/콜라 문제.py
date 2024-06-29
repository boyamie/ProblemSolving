def solution(a, b, n):
    get = 0
    now = n
    
    while (now >=a):
        namozi = now % a 
        now = (now // a)*b
        get += now
        now += namozi
    return get