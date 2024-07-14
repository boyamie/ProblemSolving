def solution(n):
    cnt = 0
    for i in range(1,n+1):
        hubo = 0
        for j in range(1,i+1):
            if i%j == 0:
                hubo +=1
        if hubo >= 3:
            cnt +=1
    return cnt