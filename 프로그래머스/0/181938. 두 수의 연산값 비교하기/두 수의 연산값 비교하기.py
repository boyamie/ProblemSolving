def solution(a, b):
    lt = [a, b]
    link = ''.join(map(str, lt))
    if int(link) == 2*a*b: 
        return link
    else:
        return max([int(link), 2*a*b]) 