def solution(x):
    under = sum([int(str(x)[i])for i in range(len(str(x)))])
    if x % under == 0:
        return True
    else:
        return False