def solution(my_string, overwrite_string, s):
    lg = len(overwrite_string)
    chg = my_string[s:s+lg]
    answer = my_string[:s]+overwrite_string+my_string[s+lg:]
    return answer