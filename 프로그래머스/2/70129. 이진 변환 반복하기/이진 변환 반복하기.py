def solution(s):
    answer=[]
    zeros = 0
    cnt = 0
    while 1:
        if s == "1":
            break
        cnt+=1
        zeros += s.count("0")
        s = s.replace("0","")
        lens = len(s)
        s = bin(len(s))[2:]
    answer.append(cnt)
    answer.append(zeros)
    return answer
            