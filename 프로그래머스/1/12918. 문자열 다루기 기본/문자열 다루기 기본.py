def solution(s):
    if len(s) != 4 and len(s) !=6:
        return False
    alp = "qwertyuiopasdfghjklzxcvbnm"
    big = alp.upper()
    for i in s:
        if i in alp:
            return False
        if i in big:
            return False
    else:
        return True