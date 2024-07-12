def solution(sides):
    sides.sort()
    m = sides.pop()
    if m < sum(sides):
        return 1
    else:
        return 2