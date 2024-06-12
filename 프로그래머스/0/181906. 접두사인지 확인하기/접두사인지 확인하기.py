def solution(my_string, is_prefix):
    lg = len(is_prefix)
    if my_string[:lg] == is_prefix:
        return 1
    else:
        return 0    