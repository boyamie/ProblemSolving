def solution(s, n):
    answer=""
    for i in s:
        if i == " ":
            answer += " "
        else:
            k = chr(ord(i)+n)
            if k.isupper() != i.isupper() or k.isalpha()==False:
                k = chr(ord(k)-26) #알파벳수 26개
            answer += k
    return answer