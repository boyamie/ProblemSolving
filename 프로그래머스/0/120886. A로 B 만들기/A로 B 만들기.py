def solution(before, after):
    for i in before:
        if before.count(i) != after.count(i):
            return 0
            break
    return 1