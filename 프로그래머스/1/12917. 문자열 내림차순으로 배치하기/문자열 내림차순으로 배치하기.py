def solution(s):
    a = ''
    big_word = s.upper()
    for i in big_word:
        if i in big_word:
            a += i
            s.replace(i, '')
    sl= list(s)
    sl.sort()
    sl.reverse()
    return ''.join(sl)