def solution(s):
    max = ""
    min = ""
    for i in s.split():
        if max == "":
            max = i
        if min == "":
            min = i
        if int(i) > int(max):
            max = i
        if int(i) < int(min):
            min = i
    return min + ' ' +max

solution("-1 -2 -3 -4")