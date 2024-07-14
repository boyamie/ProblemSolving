def solution(my_string):
    res = [i for i in my_string.lower()]
    res.sort()
    return ''.join(res)