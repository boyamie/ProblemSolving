def solution(strings, n):
    one = []
    for i in strings:
        one.append(i[n]+i)
    one.sort()
    return [i[1:] for i in one]