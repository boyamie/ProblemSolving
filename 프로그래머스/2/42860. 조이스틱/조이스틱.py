def solution(name):
    answer = 0
    alp = 0
    cur = len(name) -1
    for i, j in enumerate(name):
        alp += min(ord(j)-ord('A'), ord('Z')-ord(j)+1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        cur = min([cur,2*i+len(name)-next,i+2*(len(name)-next)])
    return alp+cur