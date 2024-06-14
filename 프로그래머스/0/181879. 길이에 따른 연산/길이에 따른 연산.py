def solution(num_list):
    leg = len(num_list)
    if leg > 10:
        return sum(num_list)
    else:
        res = 1
        for i in num_list:
            res *= i
        return res