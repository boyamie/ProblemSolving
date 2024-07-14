def solution(rsp):
    ans = ''
    for i in rsp:
        if i == '2':
            ans += '0'
        elif i == '0':
            ans += '5'
        else:
            ans += '2'
    return ans