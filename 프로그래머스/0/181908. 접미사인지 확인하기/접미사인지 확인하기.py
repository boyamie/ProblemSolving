def solution(my_string, is_suffix):
    lg = len(is_suffix)
    if my_string[-lg:] == is_suffix:
        return 1
    else:
        return 0