def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha() == False:
            answer+= int(i)
    return answer