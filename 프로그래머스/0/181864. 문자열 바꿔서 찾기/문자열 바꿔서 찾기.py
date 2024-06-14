def solution(myString, pat):
    ret = ""
    for i in myString:
        if i == "A":
            ret+="B"
        else:
            ret+="A"
    return int(pat in ret)