def solution(s):
    answer = 0
    lst = list(s.split(" "))
    stack=[]
    
    for i in lst:
        if i == 'Z':
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)